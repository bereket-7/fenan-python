from django.db import router


class NotifyController:
    def __init__(self, auth, request, redirect):
        self.auth = auth
        self.request = request
        self.redirect = redirect

    def index(self):
        # Placeholder for index logic
        pass

    def show(self):
        # Placeholder for show logic
        pass

    def store(self):
        # Check if the user is authenticated
        if not self.auth.check():
            raise PermissionError(
                'Only authenticated users can create new posts.')

        # Validate request data
        self.request.validate({
            'title': 'required',
            'body': 'required',
        })

        # Assume the authenticated user is the post's author
        author = self.auth.user()

        # Create a new post
        post = author.posts().create({
            'title': self.request.input('title'),
            'body': self.request.input('body'),
        })

        # Redirect to the post's show page
        return self.redirect(router('posts.show', post))
