from subprocess import call

print "Installing / Updating Modules..."
call(['conda', 'install', 'html5lib', 'matplotlib', 'numpy', 'scipy', 'pandas', 'scikit-learn', 'spyder'])
call(['pip', 'install', 'plyfile', 'unrar'])
