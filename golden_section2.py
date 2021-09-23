def golden_section(xA,xB,error):
    r = 0.6180333
    iteration = -1
    e = 1
    xL = xB-r*(xB-xA)
    xR = xA+r*(xB-xA)
    
    
    def function(xL, xR):
        fL = 3*xL**2-4*xL+1
        fR = 3*xR**2-4*xR+1
        return fL, fR

    def new_interval(xA,xB):
        xL = xB-r*(xB-xA)
        xR = xA+r*(xB-xA)
        return xL, xR

    def min(xA,xB,xL,xR):
        fx = function(xL, xR)
        fL = fx[0]
        fR = fx[1]
        if fR > fL:
            xB = xR
            xA = xA
            x_new = new_interval(xA,xB)
            xL = x_new[0]
            xR = x_new[1]
        elif fR < fL:
            xA = xL
            xB = xB
            x_new = new_interval(xA,xB)
            xL = x_new[0]
            xR = x_new[1]
        else:
            print('unkown error')
        return xA, xL, xR, xB
    while e > error:
        iteration = iteration + 1
        print ('Iteration: ' + str(iteration))
        print (str(xA) + ',' + str(xL)+ ',' + str(xR)+ ',' + str(xB))
        e = (abs(xB - xA)/2)
        print('Error: ', str(e))
        shift = min(xA, xB, xL, xR)
        xA = shift[0]
        xL = shift[1]
        xR = shift[2]
        xB = shift[3]
        x_new = new_interval(xA,xB)
        
        if e < error:
            x_min = (xA+xB)/2
            y_min = 3*x_min**2-4*x_min+1
            print('The minimum occurs at: (' + str(x_min) + ',' + str(y_min) + ') on iteration ' + str(iteration))
            break

golden_section(0,2,.1)
