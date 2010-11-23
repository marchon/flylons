from fabric.api import local
import logging

log = logging.getLogger('fabric')
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
log.addHandler(ch)

APP_NAME = open('./this.app.name').readline().strip()
ENV = open('./this.environment').readline().strip()

def env():
    print """
Current environment: %s
Run fab switch_env:ENV_NAME to switch.""" % ENV

def switch_env(env):
    ENV=env
    local('echo "%s" > ./this.environment' % env)

def rename_app(new_name):
    old_name = APP_NAME
    print """CAUTION: this is a pretty dumb renaming strategy: it will just replace the current all python files for the following patterns: ["from APP_NAME(...)", "import APP_NAME(...)"]. It also assumes that your source directory is in the same dir as your fabfile (may not be good if you want to use a source dir for eclipse, etc.) Intended for use when first naming your project.
"""
    if raw_input('Are you sure you want to do this[y|N]? ').lower() == 'y':
        sed_cmd = 'sed -i "{s/from[\ ]*%(old)s/from %(new)s/g;s/import[\ ]*%(old)s/import %(new)s/g;}"' % {'old': old_name, 'new': new_name} 
        
        log.info('Updating .py files in source dir...')
        local ('find ./%(old_name)s -type f -follow -name "*.py" | xargs %(sed_cmd)s' % {'sed_cmd': sed_cmd, 'old_name': old_name})
        log.info('Updating manage.py')
        local('%s manage.py' % sed_cmd)

        log.info('Moving old source dir...')
        local('mv %(old_dir)s %(new_dir)s' % {'old_dir': old_name, 'new_dir': new_name})

        log.info('Changing this.app.name for future fabric tasks')
        local("echo '%s' > ./this.app.name" % new_name)

def start():
    local('./env/bin/python manage.py runserver %s' % ENV)

def controller(name):
    template = open('%s/controllers/controller.template' % APP_NAME).read()
    controller = template % {'name': name}
    local('echo "%(controller)s" > %(app_name)s/controllers/%(filename)s.py' % 
        {'controller': controller,
        'app_name': APP_NAME,
        'filename': name}, capture=False)

