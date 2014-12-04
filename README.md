#### A responsive base theme for Wharton Django applications.
- Version: 1.0
- To be added to your Django application and customized to your needs.

##### Components & Standards: 
- Twitter Bootstrap 3
- HTML5 Boilerplate 
- HTML5 & CSS3
- SASS/SCSS (compiled via Compass)
- jQuery
- modernizer.js
- respond.js
- Fonts from fontpro.com (Open Font License)

#### Update settings.py file

##### Add the following to the bottom of your settings.py file:

<pre><code>STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
</code></pre>

##### Add the following to the 'Installed_Apps' section: 

<pre><code>'bootstrap3',
'base_theme',
</code></pre>

#### Installation via pip

1.) pip install git+https://github.com/chadwhitman/Base-Theme.git

2.) pip install django-bootstrap3 

3.) Run 'python manage.py collectstatic' to update your static files in your project directory.

Note: if you already have these apps installed, you may need to add '--upgrade' to the end of the pip install
to get the latest files.

#### Installation via Git Clone

If you don't want to pip install, you can always just clone the repo into your project and move
the files where you want them. <br />

Our stash repo: https://stash.wharton.upenn.edu/projects/WCIT/repos/django-base-theme/browse

#### If you installed Base Theme via pip, to override template files:
		
Add a 'templates' folder in your project's directory, include the template you want to <br />
override in that folder (i.e. templates/base.html) and then customize it to your needs.

#### Initial Test View/Url Configuration

This is just an example:

<pre><code>from django.views.generic import TemplateView

class BaseView(TemplateView):
    template_name = "base.html"
</code></pre>
    
And in your urls.py file:

<pre><code>from project.views import BaseView

urlpatterns = patterns('',
    url(r'^$', BaseView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
</code></pre>

#### Updating your project's stylesheets
You can update the styles via the SASS files (file extension .scss):
- Directory path --> 'static/scss/scss/example-folder/example-file.scss'

Or if you don't want to use SASS (or just need to add a few custom styles), you could add your custom styles here:
- Directory path --> 'static/scss/compiled_css/custom.css'

Note: Don't add styles to 'compiled_css/all.css' directly, as they could potentially get overwritten when SASS is compiled. 