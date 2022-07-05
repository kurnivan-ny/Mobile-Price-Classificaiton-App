from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', Classification="")

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    px_height, px_weight, pc, fc, num_cores, int_memory, ram, battery_power = [x for x in request.form.values()]

    data = []
    norm_px_height = (int(px_height)-0)/(1960-0)
    data.append(norm_px_height)
    
    norm_px_weight = (int(px_weight)-500)/(1998-500)
    data.append(norm_px_weight)

    norm_pc = (int(pc)-0)/(20-0)
    data.append(norm_pc)

    norm_fc = (int(fc)-0)/(19-0)
    data.append(norm_fc)

    norm_num_cores = (int(num_cores)-1)/(8-1)
    data.append(norm_num_cores)

    norm_int_memory = (int(int_memory)-2)/(64-2)
    data.append(norm_int_memory)

    norm_ram = (int(ram)-256)/(3998-256)
    data.append(norm_ram)

    norm_battery_power = (int(battery_power)-501)/(1998-501)
    data.append(norm_battery_power)
    
    prediction = model.predict([data])
    if prediction == 0:
        output = 'Low Cost'
    elif prediction == 1:
        output = 'Medium Cost'
    elif prediction == 2:
        output = 'High Cost'
    elif prediction == 3:
        output = 'Very High Cost'
    

    return render_template('index.html', Classification=output, px_height = px_height, px_weight = px_weight, pc = pc, fc = fc, num_cores = num_cores, int_memory = int_memory, ram = ram, battery_power = battery_power)


if __name__ == '__main__':
    app.run(debug=True)