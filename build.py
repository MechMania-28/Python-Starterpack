import zipapp
print("Writing to out.pyz...")
zipapp.create_archive('.', main='main:main', target='bot')
print("Done!")