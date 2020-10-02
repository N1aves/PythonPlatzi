>>> nombre = "Gerardo"                                                  
>>> nombre                                                              
'Gerardo'                                                               
>>> nombre[0]                                                           
'G'                                                                     
>>> nombre[1]                                                           
'e'                                                                     
>>> nombre[2]                                                           
'r'                                                                     
>>> nombre[3]                                                           
'a'                                                                     
>>> nombre[0:4]                                                         
'Gera'                                                                  
>>> nombre[:4]                                                          
'Gera'                                                                  
>>> nombre[3:]                                                          
'ardo'                                                                  
>>> nombre[4:]                                                          
'rdo'                                                                   
>>> nombre[4:0]                                                         
''                                                                      
>>> nombre[4:7]                                                         
'rdo'                                                                   
>>> nombre[4:5]                                                         
'r'                                                                     
>>> nombre[2:5]                                                         
'rar'                                                                   
>>> nombre[2:5:2]                                                       
'rr'                                                                    
>>> nombre[::2]                                                         
'Grro'                                                                  
>>> nombre[0:7:2]                                                       
'Grro'                                                                  
>>> nombre[0:7:3]                                                       
'Gao'                                                                   
>>> nombre[0:7:4]                                                       
'Gr'                                                                    
>>> nombre[0:7:1]                                                       
'Gerardo'                                                               
>>> nombre[0:7:-1]                                                      
''                                                                      
>>> nombre[::-1]                                                        
'odrareG'                                                               
>>>                                                                     