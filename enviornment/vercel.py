{
  "build": [{
    "src": "enc_dec/wsgi.py",
    "use": "@vercel/python",
    "config": {
      "maxLambdaSize": "15mb", "runtime": "python3.11.5"}
  },

     {
       "src": "build_files.sh",
      "use" : "@vercel/static-build",
      "config": {"distDir": "staticfiles_build"}
      }],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "enc_dec/wsgi.py"
    }
  ]
  
}