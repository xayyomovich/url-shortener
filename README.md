Data Flow

User visits the site and enters a long URL
The form submits to the home view
The view generates a short code for the URL
The URL and short code are saved in the database
The shortened URL is displayed to the user
When someone visits the shortened URL, the redirect_url view looks up the original URL and redirects to it