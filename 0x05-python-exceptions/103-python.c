#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - gives data of the PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	double valu = 0;
	char *stri = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	valu = ((PyFloatObject *)p)->ob_fval;
	stri = PyOS_double_to_string(valu, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  valu: %s\n", stri);
}
/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, na = 0;
	char *stri = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	stri = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying stri: %s\n", stri);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (na < size + 1 && na < 10)
	{
		printf(" %02hhx", stri[na]);
		na++;
	}
	printf("\n");
}
/**
 * print_python_list - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int na = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (na < size)
		{
			item = PyList_GET_ITEM(p, na);
			printf("Element %d: %s\n", na, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			na++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
