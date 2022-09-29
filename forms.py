from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators, SelectField, IntegerField
from wtforms.validators import NumberRange
from flask_wtf import FlaskForm
from wtforms.fields import DateField

countries = ["USA","UK","Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","The Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhutan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","CaboVerde","Cambodia","Cameroon","Canada","Central Africa","Chad","Chile","China","Colombia","Comoros","Congo","Costa Rica","Côte d’Ivoire","Croatia","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","Dominican Republic","East Timor","Timor-Leste","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Eswatini","Ethiopia","Fiji","Finland","France","Gabon","The Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","Guinea-Bissau","Guyana","Haiti","Honduras","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Korea, South","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxembourg","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Federated States of Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar","Burma","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Macedonia","Norway","Oman","Pakistan","Palau","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Romania","Russia","Rwanda","Saint Kitts","Nevis","Saint Lucia","Saint Vincent and the Grenadines","Samoa","San Marino","Sao Tome","Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovenia","Solomon Islands","Somalia","South Africa","Spain","Sri Lanka","Sudan","South,Suriname","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Togo","Tonga","Trinidad","Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates","Uruguay","Uzbekistan","Vanuatu","Vatican City","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"]

class RegForm(FlaskForm):

    currencies = ["GBP","USD","EUR", "CAD"]
    #currencies1 = ["AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BTN","BWP","BYN","BZD","CAD","CDF","CHF","CKD","CLP","CNY","COP","CRC","CUC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","FOK","GBP","GEL","GGP","GHS","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JYP","KES","KGS","KHR","KID","KMF","KPW","KRW","KWD","KZT","LAK","LBP","LKR","LRD","LSL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRU","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PND","PRB","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SGD","SEK","SGD","SHP","SLL","SLS","SRD","SSP","STN","SYP","SZL"]
    country_of_residence = SelectField(u'Country Of Residence', choices=countries, validate_choice=True)
    #country_of_residence = StringField('Country of residence', [validators.DataRequired(message='This feild is required.')])
    currency = SelectField(u'Currency', choices=currencies, validate_choice=True)
    name_first = StringField('First Name', [validators.DataRequired(message='This field is required.')])
    name_last = StringField('Last Name', [validators.DataRequired(message='This field is required.')])
    dob = DateField('entrydate', format='%Y-%m-%d' )
    email = StringField('Email Address', [validators.DataRequired(message='This field is required'), validators.Email(message='That is an invalid email adress.'), validators.Length(min=6, max=35)])
    adr1 = StringField('First Address', [validators.DataRequired(message='This field is required')])
    adr2 = StringField('Second Address', [validators.DataRequired(message='This field is required')])    
    postcode = StringField('Postcode', [validators.DataRequired(message='This field is required'),validators.Length(min = 7, max = 7)])    
    password = PasswordField('Password', [validators.DataRequired(message='You must provide a password'),validators.EqualTo('confirm', message='Passwords must match'), validators.Length(min=6, max=35)])
    confirm = PasswordField('Repeat Password')



    submit = SubmitField('Submit')


    


class LoginForm(FlaskForm):
    email = StringField('Email Address', [validators.DataRequired(), validators.Email(message='That is an invalid email adress.'), validators.Length(min=8, max=35)])
    password = PasswordField('Password', [validators.DataRequired(message='You must provide a password')])
    
    
    submit = SubmitField('Submit')

class BankForm(FlaskForm):
    cardopt = ['Visa', 'PayPal', 'MasterCard']
    cardtype = SelectField(u'Card brand', choices=cardopt, validate_choice=True)
    cardnumber = StringField('Cardnumber',[validators.DataRequired(message='This field is required')])
    cvv = StringField('CVV',[validators.DataRequired(message='This field is required'),validators.Length(min=3, max=3)])
    expirery_date = StringField('Expirery Date',[validators.DataRequired(message='This field is required')])
    b_adr1 = StringField('First Address', [validators.DataRequired(message='This field is required')])
    b_adr2 = StringField('Second Address', [validators.DataRequired(message='This field is required')])       
    b_postcode = StringField('Postcode', [validators.DataRequired(message='This field is required'),validators.Length(min = 7, max = 7)])


    amout_to_deposit = IntegerField('Amount to Deposit', [validators.DataRequired(message='This field is required'),validators.NumberRange(min=5, max=10000, message='Number must be between 5 - 10000')])
    submit = SubmitField('Submit')
    

