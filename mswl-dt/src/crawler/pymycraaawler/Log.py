''' 
     Copyright 2011 Cesar Valiente Gordo
 
     This file is part of MSWL - Development and Tools WebCrawler exercise.

    This file is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This file is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this file.  If not, see <http://www.gnu.org/licenses/>.
'''


'''
Created on 04/12/2011

@author: Cesar Valiente Gordo
@mail: cesar.valiente@gmail.com

This class is used to print log traces 
'''

class Log:
    
    _DEBUG = True
    
    """ Consturctor """
    def __init__ (self):
        pass
        
        
    """ Print a log trace if the DEBUG flag is true """            
    def d (self, className, message):
            if (self._DEBUG):
                print className + str(message)
        

            