class Emp:
    pass


class Engineer(Emp):
    pass


class PM(Emp):
    pass


class HR(Emp):
    pass


emp1 = Emp()
engineer1 = Engineer()
pm1 = PM()
hr1 = HR()
emp_classes = [Emp, Engineer, PM, HR]
staffs = [(emp1, "Employee 1"), (engineer1, "Engineer 1"),
          (pm1, "Project manager1"), (hr1, "Human resource 1")]

for staff, name in staffs:
    for emp_class in emp_classes:
        isA = isinstance(staff, emp_class)
        message1 = 'is a' if isA else 'is not a'
        print name, message1, emp_class.__name__

for class1 in emp_classes:
    for class2 in emp_classes:
        isSub = issubclass(class1, class2)
        message = '{0} a subclass of'.format('is' if isSub else 'is not')
        print class1.__name__, message, class2.__name__
