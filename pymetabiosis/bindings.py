from cffi import FFI
import sys

ffi = FFI()

ffi.cdef("""
         typedef ... PyObject;

         void Py_Initialize();
         void Py_Finalize();

         int PyRun_SimpleString(const char *command);

         void Py_INCREF(PyObject *o);
         void Py_XINCREF(PyObject *o);
         void Py_DECREF(PyObject *o);
         void Py_XDECREF(PyObject *o);

         PyObject* PyImport_ImportModule(const char *name);
         PyObject* PyErr_Occurred();
         void PyErr_Print();

         PyObject* PyObject_Str(PyObject *o);
         PyObject* PyObject_Repr(PyObject *o);
         char* PyString_AsString(PyObject *string);
         """)

lib = ffi.verify("#include<Python.h>", libraries=["python2.7"], flags=ffi.RTLD_GLOBAL)

lib.Py_Initialize()
