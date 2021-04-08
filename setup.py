from distutils.core import setup
from Cython.Build import cythonize

setup(name='Module',
      ext_modules=cythonize("D:\Manh\Source\Python\Module_Collection\draft.py"))#,
      #zip_safe = False)
#python setup.py build_ext --inplace