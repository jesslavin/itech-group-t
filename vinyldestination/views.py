from django.shortcuts import render, redirect
from django.http import HttpResponse
from vinyldestination.models import Artist, Record, Review
from vinyldestination.forms import ArtistForm, PageForm, UserForm, UserProfileForm, ReviewForm
from star_ratings.models import Rating
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.conf import settings
from social_django.models import UserSocialAuth

# Create your views here.
def index(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	
	artist_list = Artist.objects.order_by('-likes')[:5]
	record_list = Record.objects.order_by('-views')[:10]
	record_list = Record.objects.order_by('-ratings__average')[:10]
	
# Construct a dictionary to pass to the template engine as its context.
# Note the key boldmessage matches to {{ boldmessage }} in the template! 
	context_dict = {}
	context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
	context_dict['artists'] = artist_list
	context_dict['records'] = record_list
	context_dict['user_form'] = user_form
	context_dict['profile_form'] = profile_form
	visitor_cookie_handler(request)

	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier. # Note that the first parameter is the template we wish to use.
	response = render(request, 'vinyldestination/index.html', context=context_dict)
	return response

@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'vinyldestination/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'vinyldestination/password.html', {'form': form})

@login_required
def restricted(request):
	return render(request, 'vinyldestination/restricted.html', {})

# A helper method
def get_server_side_cookie(request, cookie, default_val=None): 
	val = request.session.get(cookie)
	if not val:
		val = default_val 
	return val

# Updated the function definition
def visitor_cookie_handler(request):
	visits = int(get_server_side_cookie(request, 'visits', '1')) 
	last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
	last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
	# If it's been more than a day since the last visit...
	if (datetime.now() - last_visit_time).days > 0:
		visits = visits + 1
		# Update the last visit cookie now that we have updated the count 
		request.session['last_visit'] = str(datetime.now())
	else:
		# Set the last visit cookie 
		request.session['last_visit'] = last_visit_cookie

	# Update/set the visits cookie
	request.session['visits'] = visits

@login_required
def add_category(request):
	form = CategoryForm()

	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return redirect('/vinyldestination/')
		else:
			print(form.errors)

	return render(request, 'vinyldestination/add_category.html', {'form':form})

def show_artist(request, artist_name_slug):
	context_dict = {}

	try:
		artist = Artist.objects.get(slug=artist_name_slug)

		record = Record.objects.filter(artist=artist)

		context_dict['artist'] = artist
		context_dict['records'] = record
	except Artist.DoesNotExist:
		context_dict['artist'] = None
		context_dict['records'] = None

	return render(request, 'vinyldestination/artist.html', context=context_dict)

@login_required
def add_review(request, record_name_slug):

	record = Record.objects.get(slug=record_name_slug)

	if request.method == 'POST':
		review_form = ReviewForm(request.POST)

		if review_form.is_valid():
			review = review_form.save()
			review.author = get_user_model()
			review.record = record
			review_form.save()
			return HttpResponseRedirect('/thanks/')
		else:
			print()
	else:
		review_form = ReviewForm()
	context_dict = {}
	context_dict['review_form'] = review_form
	context_dict['record'] = record
	return render(request, 'vinyldestination/add_review.html', context=context_dict)

def artists(request):
	context_dict = {}
	artist_list = Artist.objects

	context_dict['artists'] = artist_list
	visitor_cookie_handler(request)

	response = render(request, 'vinyldestination/artists.html', context=context_dict)
	return response

def records(request):
	context_dict = {}
	record_list = Record.objects.order_by('-likes')[:10]
	all_record_list = Record.objects.order_by('name')

	context_dict['records_pop'] = record_list
	context_dict['records_all'] = all_record_list

	visitor_cookie_handler(request)

	response = render(request, 'vinyldestination/records.html', context=context_dict)
	return response

def show_record(request, record_name_slug):
	context_dict = {}

	try:
		record = Record.objects.get(slug=record_name_slug)
		artist = Artist.objects.get(name=record.a_id)
		similar = Record.objects.filter(genre=record.genre).exclude(name=record.name)
		review = Review.objects.filter(record = record)

		context_dict['record'] = record
		context_dict['artist'] = artist
		context_dict['similar'] = similar
		context_dict['review'] = review
	except Record.DoesNotExist:
		context_dict['record'] = None
		context_dict['artist'] = None
		context_dict['similar'] = None
		context_dict['review'] = None


	return render(request, 'vinyldestination/record.html', context=context_dict)

def register(request):
	# A boolean value for telling the template
	# whether the registration was successful.
	# Set to False initially. Code changes value to
	# True when registration succeeds.
	registered = False

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		# If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves,
			# we set commit=False. This delays saving the model
			# until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user
			# Did the user provide a profile picture?
			# If so, we need to get it from the input form and 
			#put it in the UserProfile model.
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
				# Now we save the UserProfile model instance.
			profile.save()
				# Update our variable to indicate that the template
				# registration was successful.
			registered = True
		else:
			# Invalid form or forms - mistakes or something else?
			# Print problems to the terminal.
			print(user_form.errors, profile_form.errors)
	else:
		# Not a HTTP POST, so we render our form using two ModelForm instances. 
		# These forms will be blank, ready for user input.
		user_form = UserForm()
		profile_form = UserProfileForm()
		# Render the template depending on the context.
	return render(request, 'vinyldestination/register.html', context = {'user_form': user_form,
							'profile_form': profile_form,'registered': registered})

def user_login(request):
	# If the request is a HTTP POST, try to pull out the relevant information. 
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		# We use request.POST.get('<variable>') as opposed
		# to request.POST['<variable>'], because the
		# request.POST.get('<variable>') returns None if the
		# value does not exist, while request.POST['<variable>'] 
		# will raise a KeyError exception.
		username = request.POST.get('username')
		password = request.POST.get('password')
		# Use Django's machinery to attempt to see if the username/password 
		# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)
		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user 
		# with matching credentials was found.
		if user:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in. 
				# We'll send the user back to the homepage.
				login(request, user)
				return redirect(reverse('vinyldestination:index'))
			else:
				# An inactive account was used - no logging in!
				return HttpResponse("Your vinyldestination account is disabled.")
		else:
			# Bad login details were provided. So we can't log the user in. 
			print(f"Invalid login details: {username}, {password}")
			return HttpResponse("Invalid login details supplied.")
			# The request is not a HTTP POST, so display the login form.
			# This scenario would most likely be a HTTP GET.
	else:
		# No context variables to pass to the template system, hence the # blank dictionary object...
		return render(request, 'vinyldestination/login.html')

@login_required
def user_logout(request):
	# Since we know the user is logged in, we can now just log them out.
	logout(request)
	# Take the user back to the homepage.
	return redirect(reverse('vinyldestination:index'))
