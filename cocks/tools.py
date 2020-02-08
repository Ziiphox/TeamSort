import types




def get_functions(library):
    functions = []
    for attr_name in dir(library):
        library_object = getattr(library, attr_name)
        if isinstance(library_object, types.FunctionType):
            functions.append(library_object)
    return functions