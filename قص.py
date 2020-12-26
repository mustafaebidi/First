import random,os,sys,time


winner ="""
                 _    _ _                      >
                | |  | |_ _ __  _ __   ___ _ __
                | |/\| | | '_ \| '_ \ / _ \ '__|
                \  /\  / | | | | | | |  __/ |
                 \/  \/|_|_| |_|_| |_|\___|_|
"""

sciss = """
     ."".    ."",
     |  |   /  /
     |  |  /  /
     |  | /  /
     |  |/  ;-._
     }  ` _/  / ;
     |  /` ) /  /
     | /  /_/\_/\ 
     |/  /      |
     (  ' \ '-  |
      \    `.  /
       |      |
       |      |
       
"""
sheet = """
      __...--~~~~~-._   _.-~~~~~--...__
    //               `V'               \\
   //                 |                 \\
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
                    `---`
"""
stone = """
     ____
   _(_\  \  _____
 (____)  `|
(____)|   |
 (____).__|
  (___)__.|_____
"""


d='''
███╗░░░███╗██╗░░░██╗░██████╗████████╗░█████╗░
████╗░████║██║░░░██║██╔════╝╚══██╔══╝██╔══██╗
██╔████╔██║██║░░░██║╚█████╗░░░░██║░░░███████║
██║╚██╔╝██║██║░░░██║░╚═══██╗░░░██║░░░██╔══██║
██║░╚═╝░██║╚██████╔╝██████╔╝░░░██║░░░██║░░██║
╚═╝░░░░░╚═╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝

███████╗██████╗░██╗██████╗░
██╔════╝██╔══██╗██║██╔══██╗
█████╗░░██████╦╝██║██║░░██║
██╔══╝░░██╔══██╗██║██║░░██║
███████╗██████╦╝██║██████╔╝
╚══════╝╚═════╝░╚═╝╚═════╝░
'''

list = [stone ,  sheet , sciss]
i=[]
result=0

def mustafa():
	
	while True:
		
	    o=['box','hix','hit']
	    
	    print('''[0] To i \n[1] to h\n[2] to u''')
	
	
	    you=int(input('Entre Your namber'))
	
	    com=random.choice([0,1,2])
	    
	    def try2():
	    	
	    	for i in list:
	    		os.system('clear')
	    		print(i)
	    		time.sleep(0.7)
	    		
	    	os.system('clear')
	    	
	    	sys.stdout.write(list[you])
	    	
	    def tryy():
	    	
	    	sys.stdout.write(list[com])
	    	global result
	    	
	    	result=result+1
	    
	    def box():
	        
	        tryy()
	        
	        if o[com] == 'box' :
	        	print('draw')
	        	
	        elif o[com] == 'hix' :
	        	print('lose')
	        elif o[com] == 'hit' :
	        	print('win')
	        #if o[com] == 'box':
		        #print('draw')
           #elif o[com] == 'hix':
		        #print('win')
		    #if o[com] == 'hit' :
			    #print('lose')
			
	    def hit():
	         
	       tryy()
	       
	       if o[com] == 'hit' :
	       	print('draw')
	       if o[com] == 'box' :
	       	print('Lose')
	       if o[com] =='hix' :
	       	print('Win')
	     
		   #if o[com] == 'hit' :
			    #print('draw')
		
			
		    #if o[com] == 'box' :
			    #print('Win')
			
		    #if o[com] == 'hix' :
			    #print('lose')
			
	    def hix():
	    	tryy()
	    	
	    	if o[com] == 'hix':
	    		print('draw')
	    	if o[com] == 'box' :
	    		print('Win')
	    	if o[com] == 'hit' :
	    		print('Losr')
	    
	    if you == 0:
	        os.system('clear')
	        
	        for i in list:
	        	os.system('clear')
	        	sys.stdout.write(i)
	        	time.sleep(0.7)
	        	
	        os.system('clear')
	        #print('''          You \n         & \n       &''')
	        sys.stdout.write(list[you])
	        box()
		
	    elif you == 1:
	     
		    os.system('clear')
		    try2()
		    hix()
		
	    elif you == 2:
		    #hit()
		    os.system('clear')
		    try2()
		    hit()
		    
	    if result == 3:
	    	time.sleep(2)
	    	os.system('clear')
	    	print(winner)
	    	time.sleep(1.5)
	    	break
		  
		  
		   
		   

while True:
    os.system('clear')
    print(d)
	
    mustafa()
    
    

	

	
	