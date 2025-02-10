from django import forms

# List of states (you can modify this list as per your requirement)
STATE_CHOICES = [
    ('', 'Select your state'),  # Default "Select your state" option
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Uttarakhand', 'Uttarakhand'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Delhi', 'Delhi'),
    ('Puducherry', 'Puducherry'),
]


# Inquiry Form
class InquiryForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        label="Full Name", 
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your full name',
        })
    )
    
    email = forms.EmailField(
        label="Email", 
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email address',
        })
    )
    
    phone = forms.CharField(
        max_length=15, 
        label="Phone Number", 
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your phone number',
        })
    )
    
    age = forms.IntegerField(
        label="Age", 
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter your age',
        })
    )
    
    state = forms.ChoiceField(
        choices=STATE_CHOICES, 
        label="State", 
        widget=forms.Select(attrs={
            'placeholder': 'Select your state',
        })
    )
    
    address = forms.CharField(
        max_length=255, 
        label="Address", 
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your address',
        })
    )
    
    subject = forms.CharField(
        max_length=100, 
        label="Subject", 
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the subject of your inquiry',
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Type your inquiry message here...',
        }), 
        label="Message"
    )

    # Optional: You can define the initial value of each field here to make sure they're empty
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].initial = ''
        self.fields['email'].initial = ''
        self.fields['phone'].initial = ''
        self.fields['age'].initial = ''
        self.fields['state'].initial = ''  # No state selected initially
        self.fields['address'].initial = ''
        self.fields['subject'].initial = ''
        self.fields['message'].initial = ''
