#this program itemizes US states and their abbreviations and totals the
#the number of US states at the end of the list
states = {}
states["MA"] = "Massachusetts"
states["CA"] = "California"
states["TX"] = "Texas"
states["NJ"] = "New Jersey"
states["AL"] = "Alabama"
states["AK"] = "Alaska"
states["AZ"] = "Arizona"
states["CO"] = "Colorado"
states["CT"] = "Connecticut"
states["DE"] = "Delaware"
states["FL"] = "Florida"
states["GA"] = "Georgia"
states["HI"] = "Hawaii"
states["ID"] = "Idaho"
states["IL"] = "Illinois"
states["IN"] = "Indiana"
states["IA"] = "Iowa"
states["KS"] = "Kansas"
states["KY"] = "Kentucky"
states["LA"] = "Louisiana"
states["ME"] = "Maine"
states["MD"] = "Maryland"
states["MI"] = "Michigan"
states["MN"] = "Minnesota"
states["MS"] = "Mississippi"
states["MO"] = "Missouri"
states["MT"] = "Montana"
states["NE"] = "Nebraska"
states["NH"] = "New Hampshire"
states["NM"] = "New Mexico"
states["NY"] = "New York"
states["NC"] = "North Carolina"
states["ND"] = "North Dakota"
states["OH"] = "Ohio"
states["OK"] = "Oklahoma"
states["OR"] = "Oregon"
states["PA"] = "Pennsylvania"
states["RI"] = "Rhode Island"
states["SC"] = "South Carolina"
states["SD"] = "South Dakota"
states["TN"] = "Tennessee"
states["UT"] = "Utah"
states["VT"] = "Vermont"
states["VA"] = "Virginia"
states["WA"] = "Washington"
states["WV"] = "West Virginia"
states["WI"] = "Wisconsin"
states["WY"] = "Wyoming"

#print(states)
for key, value in states.items():
    print(key, value)
dict = states #itemized states are put in the variable dict
len(dict) #counts items
print('The number of states is:', (len(dict)))

#after much trial and error I learned to use len to count a list of items.  I learned
#puttng items into a variable first helps.
