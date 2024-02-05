from flask import Flask, render_template, request

app = Flask(__name__)

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

@app.route('/', methods=['GET', 'POST'])
def index():
    sorted_array = None
    error_message = None

    if request.method == 'POST':
        user_input = request.form['input_list']
        try:
            my_list = [int(x) for x in user_input.split()]
            bubble_sort(my_list)
            sorted_array = my_list
        except ValueError:
            error_message = "Invalid input."

    return render_template('index.html', sorted_array=sorted_array, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
