# My Blog

This is an experiment, I created a blog site and wanted to build it using cloud and serverless technologies.
For the blog, Python, Django, Wagtail and puput are used. The python code is executed with Azure Functions.

Taking advantage of the cloud environment, other services are used that are outside the scope of this repository:
* Azure DNS
* Azure CDN
* Azure Key Vaults (Site certificate and database credentials)
* Azure Storage (Static files and Database files)

![my-blog-diagram](https://github.com/Felipe1005/blog/raw/main/PipeBlogServerless.png)
