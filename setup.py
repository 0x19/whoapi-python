from setuptools import setup, find_packages

def main():
    setup(
        name             = 'whoapi',
        version          = '0.1',
        author           = 'Nevio Vesic',
        author_email     = 'me@neviovesic.com',
        license          = 'MIT',
        description      = "A python helper for whoapi service.",
        long_description = 'WhoAPI is service for mass requests of domain information like domain registration availability, structured whois data in XML and JSON, etc.',
        url              = "http://www.whoapi.com/",
        packages         = find_packages(),
        install_requires = ['requests'],
        #packages     = ['whoapi'],
        classifiers      = [
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],        
    )


if __name__ == '__main__':
    main()