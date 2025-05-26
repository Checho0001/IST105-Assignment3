import sys
import datetime

def result_steps_html(x, y, z):
    if z == 0:
        return "<p style='color:red;'>Error: value of 'z' can't be zero (division by zero).</p>"

#start respnse
    html_response = f"""
        <h2>Python Script result result :  <h2>
        <h3>Original values:</h3>
        <ul>
        <li>x : {x}</li>
        <li>y : {y}</li>
        <li>z : {z}</li>
        </ul>
        <ol>
            <li><strong>Step 1:</strong> Initial value of x = {x}</li>
        """
    #step 2
    x += y
    html_response.append(f"<li>After x += y: {x}</li>")
    #step 3
    x -= z
    html_response.append(f"<li>After x -= z: {x}</li>")
    #step 4
    x *= y
    html_response.append(f"<li>After x *= y: {x}</li>")
    #step 5
    x %= z
    html_response.append(f"<li>After x %= z: {x}</li>")
    x /= z
    html_response.append(f"<li>After x /= z: {x}</li>")
    #step 6
    final_result = x + y + z
    html_response.append(f"<li><strong>Final result</strong> x + y + z : {x} + {y} + {z} = {final_result}</li>")
    html_response.append("</ol>")

   
    
    return html_response

# read input from user
try : 
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    z = float(sys.argv[3])
except (IndexError, ValueError):
    print("Error: Input must be a number.")
    sys.exit(1)


print(result_steps_html(x, y, z))