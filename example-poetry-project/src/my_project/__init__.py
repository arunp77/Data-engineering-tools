#================================== Case-1 ===============================================
# 
# __init__.py (empty)
# Keep __init__.py Empty: If you don't need anything special, an empty __init__.py will suffice to mark the my_project directory as a package.

#=================================== Case-2 ===========================================
# 
# Import Functions Automatically: If you want the hello_world function to be available 
# directly when importing my_project, you can add this to __init__.py:

# __init__.py
from .main import hello_world

# Now, you can import the function like this in your tests or other scripts:
# from my_project import hello_world
#=====================================================================================