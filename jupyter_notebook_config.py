c.NotebookApp.log_level = 'DEBUG'

c.NotebookApp.contents_manager_class = 'jupyter_pyfilesystem.FsContentsManager'
c.ContentsManager.checkpoints_class = 'jupyter_pyfilesystem.FsCheckpoints'

import os

args = {
    'host': os.environ['OMERO_HOST'],
    'params': 'cache_ttl=120',
}
if os.getenv('OMERO_SESSION'):
    args['user'] = os.environ['OMERO_SESSION']
    args['password'] = os.environ['OMERO_SESSION']
else:
    args['user'] = os.environ['OMERO_USER']
    args['password'] = os.environ['OMERO_PASSWORD']

c.FsContentsManager.fs_url = c.FsCheckpoints.fs_url = 'omero://{user}:{password}@{host}?{params}'.format(**args)

c.FsContentsManager.keepalive = c.FsCheckpoints.keepalive = 60

