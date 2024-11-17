import telebot
from telebot import types
import matplotlib.pyplot as plt
import numpy as np
import math

# Initialize bot with token
bot = telebot.TeleBot('7383809853:AAGgEZwCu8nzqJnG_VCqynPs0Aa-FRnSBrc')

# Sample database for identification with wavelength
sample_database = {
    "Paracetamol": 243,
    "Ibuprofen": 222,
    "Aspirin": 265,
    "Ciprofloxacin": 277,
    "Atenolol": 224,
    "Metronidazole": 320,
    "Amoxicillin": 272,
    "Diclofenac Sodium": 276,
    "Ranitidine": 314,
    "Omeprazole": 305,
    "Cefixime": 288,
    "Ofloxacin": 294,
    "Sildenafil": 292,
    "Hydrochlorothiazide": 273,
    "Amlodipine": 359,
    "Clopidogrel": 220,
    "Pantoprazole": 290,
    "Lisinopril": 212,
    "Naproxen": 331,
    "Montelukast": 342,
    "Simvastatin": 238,
    "Atorvastatin": 246,
    "Tetracycline": 280,
    "Azithromycin": 215,
    "Levofloxacin": 294,
    "Fluconazole": 260,
    "Ketoconazole": 255,
    "Chloramphenicol": 278,
    "Moxifloxacin": 295,
    "Hydrocortisone": 241,
    "Indomethacin": 320,
    "Salicylic Acid": 296,
    "Ceftriaxone": 244,
    "Cefuroxime": 280,
    "Rifampicin": 475,
    "Furosemide": 274,
    "Chloroquine": 343,
    "Sulfasalazine": 365,
    "Benzocaine": 282,
    "Phenylephrine": 274,
    "Dexamethasone": 241,
    "Acyclovir": 254,
    "Trimethoprim": 237,
    "Methotrexate": 303,
    "Azathioprine": 278,
    "Piroxicam": 333,
    "Allopurinol": 250,
    "Carbamazepine": 285,
    "Fluoxetine": 226,
    "Metoprolol": 274,
    "Propranolol": 290,
    "Bromhexine": 244,
    "Theophylline": 271,
    "Gabapentin": 210,
    "Phenobarbital": 240,
    "Phenytoin": 276,
    "Erythromycin": 287,
    "Meloxicam": 364,
    "Verapamil": 278,
    "Methyldopa": 284,
    "Citalopram": 238,
    "Quinine": 350,
    "Chlorpromazine": 254,
    "Folic Acid": 283,
    "Vitamin B12 (Cobalamin)": 361,
    "Thiamine (Vitamin B1)": 245,
    "Riboflavin (Vitamin B2)": 445,
    "Nicotine": 260,
    "Retinol (Vitamin A)": 325,
    "Ascorbic Acid (Vitamin C)": 265,
    "Tocopherol (Vitamin E)": 292,
    "Lycopene": 472,
    "Water": 190,
    "Ethanol": 210,
    "Methanol": 204,
    "Acetonitrile": 190,
    "Chloroform": 240,
    "DMSO (Dimethyl Sulfoxide)": 210,
    "Acetazolamide": 267,
    "Adrenaline (Epinephrine)": 280,
    "Alprazolam": 230,
    "Amitriptyline": 242,
    "Amphotericin B": 405,
    "Baclofen": 230,
    "Betamethasone": 242,
    "Bisoprolol": 223,
    "Buspirone": 245,
    "Calcium Dobesilate": 282,
    "Carvedilol": 241,
    "Cefpodoxime": 235,
    "Cefotaxime": 235,
    "Cefdinir": 235,
    "Chlorhexidine": 260,
    "Chlorpropamide": 275,
    "Cimetidine": 218,
    "Clonazepam": 309,
    "Clotrimazole": 262,
    "Dabigatran": 270,
    "Diazepam": 235,
    "Digoxin": 220,
    "Doxazosin": 268,
    "Enalapril": 210,
    "Esomeprazole": 305,
    "Ethambutol": 292,
    "Fluticasone": 236,
    "Gliclazide": 230,
    "Glimepiride": 228,
    "Griseofulvin": 291,
    "Isoniazid": 263,
    "Ketorolac": 322,
    "Lamivudine": 270,
    "Letrozole": 242,
    "Meclizine": 243,
    "Methocarbamol": 214,
    "Metoclopramide": 308,
    "Minoxidil": 281,
    "Nifedipine": 238,
    "Nitrofurantoin": 366,
    "Olmesartan": 257,
    "Ondansetron": 310,
    "Oxytetracycline": 280,
    "Paroxetine": 290,
    "Phenylephrine HCl": 274,
    "Pindolol": 222,
    "Primaquine": 259,
    "Probenecid": 250,
    "Propofol": 269,
    "Quetiapine": 248,
    "Ribavirin": 207,
    "Rifapentine": 474,
    "Risperidone": 240,
    "Salmeterol": 229,
    "Sitagliptin": 267,
    "Sotalol": 230,
    "Spironolactone": 238,
    "Tamoxifen": 280,
    "Tenofovir": 259,
    "Terbinafine": 224,
    "Thiopental": 230,
    "Tizanidine": 228,
    "Tobramycin": 254,
    "Topiramate": 264,
    "Tranexamic Acid": 240,
    "Triamcinolone": 241,
    "Valacyclovir": 254,
    "Valsartan": 250,
    "Vardenafil": 282,
    "Venlafaxine": 274,
    "Voriconazole": 255,
    "Caffeine": 273,
    "Sulfanilamide": 257,
    "Quercetin": 370,
    "Phenol": 270,
    "Methyl Orange": 465,
    "Bromothymol Blue": 430,
    "Sodium Benzoate": 224,
    "Resorcinol": 271,
    "Nicotinamide": 262,
    "Benzyl Alcohol": 254,
    "Potassium Permanganate": 526,
    "Copper Sulfate": 809,
    "Ferric Chloride": 427,
    "Phenolphthalein": 552,
    "Erythrosine": 530,
    "Warfarin": 305,
    "Zidovudine": 267,
    "Zolpidem": 276
}

# Initialize variables to store data
wavelength = None
absorbance = None
concentration = None

# Function to display the main menu
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Input UV Readings 📊")
    btn2 = types.KeyboardButton("Absorbance to Transmittance 🔄")
    btn3 = types.KeyboardButton("Transmittance to Absorbance 🔄")
    btn4 = types.KeyboardButton("Calculate Concentration 🧪")
    btn5 = types.KeyboardButton("Find Molar Absorptivity 🧮")
    btn6 = types.KeyboardButton("Generate Graph 📈")
    btn7 = types.KeyboardButton("Identify Compound 🔍")
    btn8 = types.KeyboardButton("Clear Data 🗑️")
    btn9 = types.KeyboardButton("Help ℹ️")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    bot.send_message(message.chat.id, "Welcome! Choose an option from the menu below:", reply_markup=markup)

# Start Command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello! I am your UV Spectrophotometer Assistant. What would you like to do today?")
    main_menu(message)

# Handle User's Input
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Input UV Readings 📊":
        bot.send_message(message.chat.id, "Please enter wavelength and absorbance values in the format: wavelength, absorbance (e.g., 243, 1.2)")
        bot.register_next_step_handler(message, process_readings)
    elif message.text == "Absorbance to Transmittance 🔄":
        bot.send_message(message.chat.id, "Please enter absorbance value to convert to transmittance:")
        bot.register_next_step_handler(message, absorbance_to_transmittance)
    elif message.text == "Transmittance to Absorbance 🔄":
        bot.send_message(message.chat.id, "Please enter transmittance value (%T) to convert to absorbance:")
        bot.register_next_step_handler(message, transmittance_to_absorbance)
    elif message.text == "Calculate Concentration 🧪":
        if absorbance and wavelength:
            calculate_concentration(message)
        else:
            bot.send_message(message.chat.id, "Please input UV readings first.")
    elif message.text == "Find Molar Absorptivity 🧮":
        if concentration:
            find_molar_absorptivity(message)
        else:
            bot.send_message(message.chat.id, "Please calculate the concentration first.")
    elif message.text == "Generate Graph 📈":
        bot.send_message(message.chat.id, "Enter absorbance values separated by commas (e.g., 1.2, 1.3, 1.5).")
        bot.register_next_step_handler(message, generate_graph)
    elif message.text == "Identify Compound 🔍":
        bot.send_message(message.chat.id, "Please enter the wavelength value for identification.")
        bot.register_next_step_handler(message, identify_sample)
    elif message.text == "Clear Data 🗑️":
        clear_data(message)
    elif message.text == "Help ℹ️":
        bot.send_message(message.chat.id, "Here’s how to use this bot:\n1. Input UV readings for concentration.\n2. Convert absorbance to transmittance or vice versa.\n3. Generate graphs of absorbance vs wavelength.\n4. Identify samples based on wavelength.")
        main_menu(message)
    else:
        bot.send_message(message.chat.id, "I didn't understand that. Please choose an option from the main menu.")
        main_menu(message)

# Process UV Readings
def process_readings(message):
    global wavelength, absorbance
    try:
        values = message.text.split(',')
        wavelength = float(values[0].strip())
        absorbance = float(values[1].strip())
        bot.send_message(message.chat.id, f"Data input successful: Wavelength = {wavelength} nm, Absorbance = {absorbance}")
        main_menu(message)
    except Exception as e:
        bot.send_message(message.chat.id, "There was an error processing the data. Please enter the values in the correct format.")
        main_menu(message)

# Convert Absorbance to Transmittance
def absorbance_to_transmittance(message):
    try:
        absorbance = float(message.text.strip())
        transmittance = 10 ** (2 - absorbance)
        bot.send_message(message.chat.id, f"Transmittance: {transmittance:.2f}%")
        main_menu(message)
    except Exception as e:
        bot.send_message(message.chat.id, "Error converting absorbance to transmittance. Please enter a valid absorbance value.")
        main_menu(message)

# Convert Transmittance to Absorbance
def transmittance_to_absorbance(message):
    try:
        transmittance = float(message.text.strip())
        absorbance = 2 - math.log10(transmittance)
        bot.send_message(message.chat.id, f"Absorbance: {absorbance:.2f}")
        main_menu(message)
    except Exception as e:
        bot.send_message(message.chat.id, "Error converting transmittance to absorbance. Please enter a valid transmittance value.")
        main_menu(message)

# Calculate Concentration
def calculate_concentration(message):
    global concentration
    try:
        closest_match = None
        min_diff = float('inf')
        for sample, wl in sample_database.items():
            diff = abs(wl - wavelength)
            if diff < min_diff:
                min_diff = diff
                closest_match = sample

        if closest_match:
            epsilon = 100  # Placeholder, replace with actual molar absorptivity if known for each sample
            path_length = 1.0  # Path length is 1 cm by default
            concentration = absorbance / (epsilon * path_length)
            bot.send_message(message.chat.id, f"Sample identified: {closest_match}\nConcentration calculated: {concentration:.5f} mol/L")
        else:
            bot.send_message(message.chat.id, "No match found for the wavelength in the database.")
        main_menu(message)
    except Exception as e:
        bot.send_message(message.chat.id, "Error calculating concentration. Ensure absorbance and wavelength are correct.")
        main_menu(message)

# Find Molar Absorptivity
def find_molar_absorptivity(message):
    try:
        epsilon = absorbance / (concentration * 1.0)  # Path length is assumed to be 1 cm
        bot.send_message(message.chat.id, f"Molar Absorptivity: {epsilon:.2f} L/(mol·cm)")
        main_menu(message)
    except Exception as e:
        bot.send_message(message.chat.id, "Error calculating molar absorptivity.")
        main_menu(message)

# Generate Graph from Absorbance Data
def generate_graph(message):
    try:
        absorbance_values = list(map(float, message.text.split(',')))
        wavelengths = np.arange(200, 200 + len(absorbance_values) * 10, 10)
        plt.plot(wavelengths, absorbance_values, marker='o')
        plt.xlabel('Wavelength (nm)')
        plt.ylabel('Absorbance')
        plt.title('Absorbance vs Wavelength')
        plt.grid(True)
        plt.savefig('graph.png')
        plt.close()

        with open('graph.png', 'rb') as graph:
            bot.send_photo(message.chat.id, graph)
        main_menu(message)
    except Exception as e:
        bot.send_message(message.chat.id, "There was an error generating the graph. Please enter correct absorbance values.")
        main_menu(message)

# Identify Sample Based on Wavelength
def identify_sample(message):
    try:
        wavelength = float(message.text.strip())
        closest_match = None
        min_diff = float('inf')
        for sample, wl in sample_database.items():
            diff = abs(wl - wavelength)
            if diff < min_diff:
                min_diff = diff
                closest_match = sample
        if closest_match:
            bot.send_message(message.chat.id, f"The closest match is: {closest_match} (wavelength: {sample_database[closest_match]} nm)")
        else:
            bot.send_message(message.chat.id, "No match found in the database.")
        main_menu(message)
    except Exception as e:
        bot.send_message(message.chat.id, "Error in identifying the sample. Please enter a valid wavelength value.")
        main_menu(message)

# Clear Data
def clear_data(message):
    global wavelength, absorbance, concentration
    wavelength = None
    absorbance = None
    concentration = None
    bot.send_message(message.chat.id, "Data cleared successfully!")
    main_menu(message)

# Run the bot
bot.polling()
