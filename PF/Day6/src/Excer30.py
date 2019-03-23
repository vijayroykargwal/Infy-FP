#PF-Exer-30
'''
Created on Feb 27, 2019

@author: vijay.pal01
'''
from builtins import int




def find_average(mark_list):
    total=0
    
    try: 
         
        for i in range(0, len(mark_list)):
            total += mark_list[i]
        marks_avg=total/len(mark_list)
        return marks_avg
    except ZeroDivisionError:
        print("Zero Division Error has been occurred")
         
    except TypeError:
        print("Type Error has been Occurred")
    except NameError:
        print("Name Error has been Occurred")
    except ValueError:
        print("Value Error has been Occurred")
    except IndexError:
        print("Index Error has been Occurred")
    finally:
         
        print("Program Ends Here")
         


m_list=[1,2,3,4]
print("Average marks:", find_average(m_list))
