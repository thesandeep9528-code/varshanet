"""
Indian states and districts with approximate geographic coordinates.
Used for generating spatial forecast data across India.
"""

INDIAN_STATES = {
    "Andhra Pradesh": ["Visakhapatnam", "Vijayawada", "Guntur", "Nellore", "Kurnool", "Kadapa", "Tirupati", "Rajahmundry", "Anantapur", "Kakinada"],
    "Arunachal Pradesh": ["Itanagar", "Tawang", "Ziro", "Pasighat", "Roing", "Tezu", "Bomdila", "Along", "Daporijo", "Khonsa"],
    "Assam": ["Guwahati", "Silchar", "Dibrugarh", "Jorhat", "Nagaon", "Tinsukia", "Tezpur", "Bongaigaon", "Diphu", "Dhubri"],
    "Bihar": ["Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Purnia", "Darbhanga", "Ara", "Begusarai", "Katihar", "Munger"],
    "Chhattisgarh": ["Raipur", "Bhilai", "Bilaspur", "Korba", "Rajnandgaon", "Raigarh", "Jagdalpur", "Ambikapur", "Durg", "Mahasamund"],
    "Goa": ["North Goa", "South Goa", "Panaji", "Margao", "Vasco da Gama", "Mapusa", "Ponda", "Bicholim", "Curchorem", "Sanquelim"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar", "Junagadh", "Gandhinagar", "Anand", "Navsari"],
    "Haryana": ["Faridabad", "Gurugram", "Panipat", "Ambala", "Yamunanagar", "Rohtak", "Hisar", "Karnal", "Sonipat", "Panchkula"],
    "Himachal Pradesh": ["Shimla", "Mandi", "Dharamshala", "Solan", "Kullu", "Chamba", "Bilaspur", "Hamirpur", "Una", "Sirmaur"],
    "Jharkhand": ["Ranchi", "Jamshedpur", "Dhanbad", "Bokaro", "Deoghar", "Hazaribagh", "Giridih", "Ramgarh", "Medininagar", "Dumka"],
    "Karnataka": ["Bengaluru", "Mysuru", "Hubballi-Dharwad", "Mangaluru", "Belagavi", "Kalaburagi", "Davanagere", "Ballari", "Vijayapura", "Shivamogga"],
    "Kerala": ["Thiruvananthapuram", "Kochi", "Kozhikode", "Kollam", "Thrissur", "Alappuzha", "Palakkad", "Kannur", "Kottayam", "Malappuram"],
    "Madhya Pradesh": ["Indore", "Bhopal", "Jabalpur", "Gwalior", "Ujjain", "Sagar", "Dewas", "Satna", "Ratlam", "Rewa"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad", "Solapur", "Amravati", "Nanded", "Kolhapur", "Sangli"],
    "Manipur": ["Imphal", "Thoubal", "Bishnupur", "Churachandpur", "Ukhrul", "Senapati", "Tamenglong", "Chandel", "Jiribam", "Kakching"],
    "Meghalaya": ["Shillong", "Tura", "Jowai", "Nongpoh", "Williamnagar", "Baghmara", "Resubelpara", "Mairang", "Khliehriat", "Ampati"],
    "Mizoram": ["Aizawl", "Lunglei", "Saiha", "Champhai", "Kolasib", "Serchhip", "Lawngtlai", "Mamit", "Hnahthial", "Khawzawl"],
    "Nagaland": ["Kohima", "Dimapur", "Mokokchung", "Tuensang", "Wokha", "Zunheboto", "Kiphire", "Mon", "Phek", "Longleng"],
    "Odisha": ["Bhubaneswar", "Cuttack", "Rourkela", "Brahmapur", "Sambalpur", "Puri", "Balasore", "Bhadrak", "Baripada", "Jharsuguda"],
    "Punjab": ["Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Bathinda", "Mohali", "Hoshiarpur", "Batala", "Pathankot", "Moga"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Kota", "Bikaner", "Ajmer", "Udaipur", "Bhilwara", "Alwar", "Bharatpur", "Sikar"],
    "Sikkim": ["Gangtok", "Namchi", "Geyzing", "Mangan", "Pakyong", "Soreng", "Singtam", "Rangpo", "Jorethang", "Nayabazar"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Tiruppur", "Salem", "Erode", "Tirunelveli", "Vellore", "Thoothukudi"],
    "Telangana": ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Ramagundam", "Khammam", "Mahbubnagar", "Nalgonda", "Adilabad", "Suryapet"],
    "Tripura": ["Agartala", "Udaipur", "Dharmanagar", "Kailashahar", "Belonia", "Khowai", "Ambassa", "Bishalgarh", "Santirbazar", "Melaghar"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra", "Varanasi", "Meerut", "Prayagraj", "Ghaziabad", "Bareilly", "Aligarh", "Moradabad"],
    "Uttarakhand": ["Dehradun", "Haridwar", "Roorkee", "Haldwani", "Rudrapur", "Kashipur", "Rishikesh", "Pithoragarh", "Ramnagar", "Manglaur"],
    "West Bengal": ["Kolkata", "Asansol", "Siliguri", "Durgapur", "Bardhaman", "Malda", "Baharampur", "Habra", "Kharagpur", "Shantipur"],
    "Andaman and Nicobar Islands": ["Port Blair", "Car Nicobar", "Mayabunder", "Hut Bay", "Diglipur", "Rangat", "Ferrargunj", "Garacharma", "Bambooflat", "Prothrapur"],
    "Chandigarh": ["Chandigarh", "Mani Majra", "Burail", "Attawa", "Kajheri", "Khuda Alisher", "Dhanas", "Maloya", "Sarangpur", "Kishangarh"],
    "Dadra and Nagar Haveli and Daman and Diu": ["Daman", "Diu", "Silvassa", "Amli", "Bhimpore", "Dadra", "Kachigam", "Kadaiya", "Marwad", "Dunetha"],
    "Delhi": ["New Delhi", "North Delhi", "South Delhi", "East Delhi", "West Delhi", "Central Delhi", "Shahdara", "Rohini", "Dwarka", "Vasant Kunj"],
    "Jammu and Kashmir": ["Srinagar", "Jammu", "Anantnag", "Baramulla", "Kathua", "Sopore", "Pulwama", "Udhampur", "Poonch", "Kupwara"],
    "Ladakh": ["Leh", "Kargil", "Nubra", "Zanskar", "Dras", "Khaltsi", "Nyoma", "Sankoo", "Padum", "Diskit"],
    "Lakshadweep": ["Kavaratti", "Agatti", "Amini", "Andrott", "Bitra", "Chetlat", "Kadmat", "Kalpeni", "Kiltan", "Minicoy"],
    "Puducherry": ["Puducherry", "Ozhukarai", "Karaikal", "Yanam", "Mahe", "Villianur", "Ariyankuppam", "Kurumbapet", "Thirunallar", "Bahour"]
}


# Approximate (lat, lon) coordinates for major Indian districts/cities
DISTRICT_COORDS = {
    # Andhra Pradesh
    "Visakhapatnam": (17.69, 83.22), "Vijayawada": (16.51, 80.65), "Guntur": (16.31, 80.44),
    "Nellore": (14.45, 79.99), "Kurnool": (15.83, 78.04), "Kadapa": (14.47, 78.82),
    "Tirupati": (13.63, 79.42), "Rajahmundry": (17.00, 81.80), "Anantapur": (14.68, 77.60),
    "Kakinada": (16.94, 82.24),
    # Arunachal Pradesh
    "Itanagar": (27.10, 93.62), "Tawang": (27.59, 91.86), "Ziro": (27.54, 93.83),
    "Pasighat": (28.07, 95.33), "Roing": (28.14, 95.84), "Tezu": (27.93, 96.17),
    "Bomdila": (27.26, 92.42), "Along": (28.17, 94.77), "Daporijo": (27.99, 94.22),
    "Khonsa": (27.02, 95.50),
    # Assam
    "Guwahati": (26.14, 91.74), "Silchar": (24.83, 92.80), "Dibrugarh": (27.47, 94.91),
    "Jorhat": (26.76, 94.22), "Nagaon": (26.35, 92.69), "Tinsukia": (27.49, 95.37),
    "Tezpur": (26.63, 92.80), "Bongaigaon": (26.48, 90.56), "Diphu": (25.84, 93.43),
    "Dhubri": (26.02, 89.97),
    # Bihar
    "Patna": (25.61, 85.14), "Gaya": (24.80, 85.01), "Bhagalpur": (25.24, 86.97),
    "Muzaffarpur": (26.12, 85.39), "Purnia": (25.78, 87.47), "Darbhanga": (26.15, 85.90),
    "Ara": (25.56, 84.66), "Begusarai": (25.42, 86.13), "Katihar": (25.54, 87.57),
    "Munger": (25.38, 86.47),
    # Chhattisgarh
    "Raipur": (21.25, 81.63), "Bhilai": (21.21, 81.38), "Bilaspur": (22.08, 82.15),
    "Korba": (22.35, 82.68), "Rajnandgaon": (21.10, 81.03), "Raigarh": (21.90, 83.40),
    "Jagdalpur": (19.08, 82.02), "Ambikapur": (23.12, 83.20), "Durg": (21.19, 81.28),
    "Mahasamund": (21.11, 82.10),
    # Goa
    "North Goa": (15.53, 73.96), "South Goa": (15.28, 74.08), "Panaji": (15.50, 73.83),
    "Margao": (15.27, 73.96), "Vasco da Gama": (15.40, 73.81), "Mapusa": (15.59, 73.81),
    "Ponda": (15.40, 74.01), "Bicholim": (15.60, 73.95), "Curchorem": (15.26, 74.11),
    "Sanquelim": (15.56, 74.01),
    # Gujarat
    "Ahmedabad": (23.02, 72.57), "Surat": (21.17, 72.83), "Vadodara": (22.31, 73.19),
    "Rajkot": (22.30, 70.78), "Bhavnagar": (21.76, 72.15), "Jamnagar": (22.47, 70.07),
    "Junagadh": (21.52, 70.46), "Gandhinagar": (23.22, 72.68), "Anand": (22.56, 72.93),
    "Navsari": (20.95, 72.95),
    # Haryana
    "Faridabad": (28.41, 77.31), "Gurugram": (28.46, 77.03), "Panipat": (29.39, 76.97),
    "Ambala": (30.38, 76.78), "Yamunanagar": (30.13, 77.29), "Rohtak": (28.90, 76.57),
    "Hisar": (29.15, 75.72), "Karnal": (29.69, 76.98), "Sonipat": (28.99, 77.02),
    "Panchkula": (30.69, 76.86),
    # Himachal Pradesh
    "Shimla": (31.10, 77.17), "Mandi": (31.72, 76.93), "Dharamshala": (32.22, 76.32),
    "Solan": (30.91, 77.10), "Kullu": (31.96, 77.11), "Chamba": (32.56, 76.13),
    "Bilaspur": (31.34, 76.76), "Hamirpur": (31.69, 76.52), "Una": (31.47, 76.27),
    "Sirmaur": (30.57, 77.30),
    # Jharkhand
    "Ranchi": (23.34, 85.31), "Jamshedpur": (22.80, 86.20), "Dhanbad": (23.79, 86.43),
    "Bokaro": (23.67, 86.15), "Deoghar": (24.49, 86.69), "Hazaribagh": (23.99, 85.36),
    "Giridih": (24.19, 86.30), "Ramgarh": (23.63, 85.52), "Medininagar": (24.21, 84.07),
    "Dumka": (24.27, 87.25),
    # Karnataka
    "Bengaluru": (12.97, 77.59), "Mysuru": (12.30, 76.64), "Hubballi-Dharwad": (15.36, 75.12),
    "Mangaluru": (12.87, 74.84), "Belagavi": (15.85, 74.50), "Kalaburagi": (17.33, 76.83),
    "Davanagere": (14.47, 75.92), "Ballari": (15.14, 76.92), "Vijayapura": (16.83, 75.72),
    "Shivamogga": (13.93, 75.57),
    # Kerala
    "Thiruvananthapuram": (8.52, 76.94), "Kochi": (9.93, 76.27), "Kozhikode": (11.25, 75.77),
    "Kollam": (8.89, 76.60), "Thrissur": (10.53, 76.21), "Alappuzha": (9.49, 76.34),
    "Palakkad": (10.78, 76.65), "Kannur": (11.87, 75.37), "Kottayam": (9.59, 76.52),
    "Malappuram": (11.07, 76.07),
    # Madhya Pradesh
    "Indore": (22.72, 75.86), "Bhopal": (23.26, 77.41), "Jabalpur": (23.18, 79.95),
    "Gwalior": (26.22, 78.18), "Ujjain": (23.18, 75.77), "Sagar": (23.84, 78.74),
    "Dewas": (22.97, 76.05), "Satna": (24.58, 80.83), "Ratlam": (23.33, 75.04),
    "Rewa": (24.53, 81.30),
    # Maharashtra
    "Mumbai": (19.08, 72.88), "Pune": (18.52, 73.86), "Nagpur": (21.15, 79.09),
    "Nashik": (20.00, 73.79), "Aurangabad": (19.88, 75.34), "Solapur": (17.68, 75.91),
    "Amravati": (20.93, 77.77), "Nanded": (19.16, 77.32), "Kolhapur": (16.70, 74.24),
    "Sangli": (16.85, 74.56),
    # Manipur
    "Imphal": (24.82, 93.95), "Thoubal": (24.64, 94.01), "Bishnupur": (24.63, 93.78),
    "Churachandpur": (24.33, 93.68), "Ukhrul": (25.12, 94.37), "Senapati": (25.27, 94.02),
    "Tamenglong": (24.98, 93.51), "Chandel": (24.32, 94.03), "Jiribam": (24.79, 93.12),
    "Kakching": (24.50, 93.98),
    # Meghalaya
    "Shillong": (25.57, 91.88), "Tura": (25.51, 90.22), "Jowai": (25.45, 92.20),
    "Nongpoh": (25.90, 91.88), "Williamnagar": (25.49, 90.62), "Baghmara": (25.22, 90.63),
    "Resubelpara": (25.90, 90.58), "Mairang": (25.55, 91.56), "Khliehriat": (25.34, 92.34),
    "Ampati": (25.25, 90.28),
    # Mizoram
    "Aizawl": (23.73, 92.72), "Lunglei": (22.88, 92.74), "Saiha": (22.49, 92.98),
    "Champhai": (23.47, 93.33), "Kolasib": (24.23, 92.68), "Serchhip": (23.30, 92.84),
    "Lawngtlai": (22.53, 92.90), "Mamit": (23.93, 92.49), "Hnahthial": (22.78, 92.79),
    "Khawzawl": (23.35, 93.15),
    # Nagaland
    "Kohima": (25.67, 94.12), "Dimapur": (25.90, 93.73), "Mokokchung": (26.32, 94.52),
    "Tuensang": (26.27, 94.83), "Wokha": (26.10, 94.27), "Zunheboto": (25.97, 94.52),
    "Kiphire": (25.88, 94.97), "Mon": (26.75, 95.00), "Phek": (25.67, 94.47),
    "Longleng": (26.42, 94.87),
    # Odisha
    "Bhubaneswar": (20.30, 85.82), "Cuttack": (20.46, 85.89), "Rourkela": (22.26, 84.85),
    "Brahmapur": (19.31, 84.79), "Sambalpur": (21.47, 83.97), "Puri": (19.81, 85.83),
    "Balasore": (21.49, 86.93), "Bhadrak": (21.05, 86.50), "Baripada": (21.93, 86.73),
    "Jharsuguda": (21.86, 84.01),
    # Punjab
    "Ludhiana": (30.90, 75.86), "Amritsar": (31.63, 74.87), "Jalandhar": (31.33, 75.58),
    "Patiala": (30.34, 76.39), "Bathinda": (30.21, 74.95), "Mohali": (30.70, 76.72),
    "Hoshiarpur": (31.53, 75.91), "Batala": (31.82, 75.20), "Pathankot": (32.27, 75.65),
    "Moga": (30.82, 75.17),
    # Rajasthan
    "Jaipur": (26.92, 75.79), "Jodhpur": (26.29, 73.02), "Kota": (25.18, 75.86),
    "Bikaner": (28.02, 73.31), "Ajmer": (26.45, 74.64), "Udaipur": (24.58, 73.68),
    "Bhilwara": (25.35, 74.63), "Alwar": (27.56, 76.63), "Bharatpur": (27.22, 77.49),
    "Sikar": (27.61, 75.14),
    # Sikkim
    "Gangtok": (27.33, 88.62), "Namchi": (27.17, 88.35), "Geyzing": (27.19, 88.26),
    "Mangan": (27.51, 88.53), "Pakyong": (27.24, 88.61), "Soreng": (27.15, 88.18),
    "Singtam": (27.23, 88.50), "Rangpo": (27.18, 88.53), "Jorethang": (27.10, 88.32),
    "Nayabazar": (27.09, 88.19),
    # Tamil Nadu
    "Chennai": (13.08, 80.27), "Coimbatore": (11.00, 76.96), "Madurai": (9.93, 78.12),
    "Tiruchirappalli": (10.79, 78.69), "Tiruppur": (11.11, 77.35), "Salem": (11.66, 78.15),
    "Erode": (11.34, 77.72), "Tirunelveli": (8.73, 77.70), "Vellore": (12.92, 79.13),
    "Thoothukudi": (8.76, 78.14),
    # Telangana
    "Hyderabad": (17.39, 78.49), "Warangal": (17.98, 79.60), "Nizamabad": (18.67, 78.09),
    "Karimnagar": (18.44, 79.13), "Ramagundam": (18.76, 79.47), "Khammam": (17.25, 80.15),
    "Mahbubnagar": (16.74, 77.99), "Nalgonda": (17.05, 79.27), "Adilabad": (19.67, 78.53),
    "Suryapet": (17.14, 79.62),
    # Tripura
    "Agartala": (23.83, 91.28), "Udaipur": (23.53, 91.48), "Dharmanagar": (24.38, 92.17),
    "Kailashahar": (24.33, 92.01), "Belonia": (23.25, 91.46), "Khowai": (24.06, 91.60),
    "Ambassa": (23.92, 91.84), "Bishalgarh": (23.63, 91.30), "Santirbazar": (23.32, 91.79),
    "Melaghar": (23.59, 91.22),
    # Uttar Pradesh
    "Lucknow": (26.85, 80.95), "Kanpur": (26.45, 80.35), "Agra": (27.18, 78.02),
    "Varanasi": (25.32, 83.01), "Meerut": (28.98, 77.71), "Prayagraj": (25.43, 81.85),
    "Ghaziabad": (28.67, 77.42), "Bareilly": (28.37, 79.42), "Aligarh": (27.88, 78.08),
    "Moradabad": (28.84, 78.78),
    # Uttarakhand
    "Dehradun": (30.32, 78.03), "Haridwar": (29.95, 78.16), "Roorkee": (29.87, 77.89),
    "Haldwani": (29.22, 79.52), "Rudrapur": (28.97, 79.40), "Kashipur": (29.21, 78.96),
    "Rishikesh": (30.09, 78.27), "Pithoragarh": (29.58, 80.22), "Ramnagar": (29.39, 79.13),
    "Manglaur": (29.79, 77.87),
    # West Bengal
    "Kolkata": (22.57, 88.36), "Asansol": (23.68, 86.99), "Siliguri": (26.72, 88.43),
    "Durgapur": (23.55, 87.32), "Bardhaman": (23.23, 87.87), "Malda": (25.01, 88.14),
    "Baharampur": (24.10, 88.25), "Habra": (22.84, 88.63), "Kharagpur": (22.33, 87.32),
    "Shantipur": (23.25, 88.43),
    # Andaman and Nicobar Islands
    "Port Blair": (11.67, 92.74), "Car Nicobar": (9.15, 92.77), "Mayabunder": (12.93, 92.90),
    "Hut Bay": (10.60, 92.57), "Diglipur": (13.27, 93.00), "Rangat": (12.50, 92.92),
    "Ferrargunj": (11.58, 92.75), "Garacharma": (11.60, 92.71), "Bambooflat": (11.60, 92.72),
    "Prothrapur": (11.62, 92.73),
    # Chandigarh
    "Chandigarh": (30.73, 76.78), "Mani Majra": (30.73, 76.82), "Burail": (30.72, 76.76),
    "Attawa": (30.74, 76.80), "Kajheri": (30.69, 76.78), "Khuda Alisher": (30.74, 76.83),
    "Dhanas": (30.76, 76.75), "Maloya": (30.68, 76.76), "Sarangpur": (30.72, 76.77),
    "Kishangarh": (30.75, 76.81),
    # DNH and DD
    "Daman": (20.41, 72.85), "Diu": (20.71, 70.99), "Silvassa": (20.27, 73.00),
    "Amli": (20.28, 73.02), "Bhimpore": (20.39, 72.86), "Dadra": (20.33, 73.16),
    "Kachigam": (20.28, 73.01), "Kadaiya": (20.34, 73.15), "Marwad": (20.35, 73.12),
    "Dunetha": (20.36, 73.10),
    # Delhi
    "New Delhi": (28.61, 77.21), "North Delhi": (28.72, 77.20), "South Delhi": (28.53, 77.22),
    "East Delhi": (28.63, 77.28), "West Delhi": (28.65, 77.10), "Central Delhi": (28.64, 77.22),
    "Shahdara": (28.67, 77.29), "Rohini": (28.74, 77.11), "Dwarka": (28.57, 77.05),
    "Vasant Kunj": (28.52, 77.16),
    # Jammu and Kashmir
    "Srinagar": (34.08, 74.80), "Jammu": (32.73, 74.87), "Anantnag": (33.73, 75.15),
    "Baramulla": (34.20, 74.34), "Kathua": (32.38, 75.52), "Sopore": (34.30, 74.47),
    "Pulwama": (33.87, 74.90), "Udhampur": (32.93, 75.14), "Poonch": (33.77, 74.09),
    "Kupwara": (34.53, 74.27),
    # Ladakh
    "Leh": (34.16, 77.58), "Kargil": (34.56, 76.13), "Nubra": (34.68, 77.57),
    "Zanskar": (33.50, 76.86), "Dras": (34.43, 75.76), "Khaltsi": (34.30, 76.88),
    "Nyoma": (33.18, 78.64), "Sankoo": (34.33, 76.23), "Padum": (33.46, 76.89),
    "Diskit": (34.55, 77.56),
    # Lakshadweep
    "Kavaratti": (10.57, 72.64), "Agatti": (10.85, 72.20), "Amini": (11.12, 72.73),
    "Andrott": (10.82, 73.68), "Bitra": (11.58, 72.10), "Chetlat": (11.70, 72.71),
    "Kadmat": (11.23, 72.78), "Kalpeni": (10.08, 73.65), "Kiltan": (11.48, 73.00),
    "Minicoy": (8.27, 73.04),
    # Puducherry
    "Puducherry": (11.93, 79.83), "Ozhukarai": (11.95, 79.77), "Karaikal": (10.93, 79.84),
    "Yanam": (16.73, 82.21), "Mahe": (11.70, 75.54), "Villianur": (11.93, 79.77),
    "Ariyankuppam": (11.90, 79.83), "Kurumbapet": (11.92, 79.80), "Thirunallar": (10.94, 79.83),
    "Bahour": (11.81, 79.74),
}


def get_districts_by_state(state: str) -> list:
    """Returns list of districts for a given state."""
    return INDIAN_STATES.get(state, [])


def get_all_districts() -> list:
    """Returns a flat list of all districts."""
    districts = []
    for dist_list in INDIAN_STATES.values():
        districts.extend(dist_list)
    return districts
