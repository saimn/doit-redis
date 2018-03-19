from setuptools import setup

setup(
    name='doit-redis',
    version='0.1',
    license='MIT',
    author='Simon Conseil',
    author_email='contact@saimon.org',
    url='http://github.com/saimn/doit-redis',
    description='Redis backend for doit',
    long_description=open('README.md').read(),
    py_modules=['doit_redis'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    python_requires='>=3.5',
    keywords=['doit'],
    install_requires=['doit', 'redis'],
    entry_points={
        'doit.BACKEND': [
            'redis = doit_redis:RedisDB'
        ]
    },
)
