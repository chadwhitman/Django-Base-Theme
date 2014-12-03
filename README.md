#### A responsive base theme for Wharton Django applications.
- Version: 1.0
- To be added to your Django application and customized to your needs.

##### Technologies: 
- Twitter Bootstrap
- HTML5 Boilerplate 
- HTML5 & CSS3
- SASS/SCSS (compiled via Compass)
- jQuery
- modernizer.js
- respond.js
- fonts from fontpro.com

#### Update settings.py file

##### Add the following to the 'Installed_Apps' section: 

<pre><code>'bootstrap3',
'base_theme',
</code></pre>

##### Add the following to the bottom of your settings.py file:

<pre><code>STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
</code></pre>

#### Installation via pip

1.) pip install git+https://github.com/chadwhitman/Base-Theme.git

2.) Add 'base_theme' to 'Installed Apps' in your project's 'settings.py' file.

3.) Run 'python manage.py collectstatic' to update your static files in your project directory.

4.) pip install django-bootstrap3

#### Installation via Git Clone

If you don't want to pip install, you can always just clone the repo into your project and move
the files where you want them.

#### If you installed via pip, to override template files:
		
Add a 'templates' folder in your project's directory, include the template you want to <br />
override in that folder (i.e. base.html) and then customize it to your needs.

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