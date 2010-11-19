from fabric.api import local

APP_NAME = open('./this.app.name').readline().strip()
ENV = open('./this.environment').readline().strip()

def env():
    print """
Current environment: %s
Run fab switch_env:ENV_NAME to switch.""" % ENV

def switch_env(env):
    ENV=env
    local('echo "%s" > ./this.environment' % env)

def start():
    local('./env/bin/python manage.py runserver %s' % ENV)

def controller(name):
    template = open('%s/controllers/controller.template' % APP_NAME).read()
    controller = template % {'name': name}
    local('echo "%(controller)s" > %(app_name)s/controllers/%(filename)s.py' % 
        {'controller': controller,
        'app_name': APP_NAME,
        'filename': name}, capture=False)


