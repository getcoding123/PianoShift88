#PianoShift88
#Selection and variables
select = input("Would You Like to Encode or Decode?")
codeAlphabet = ["A0", "B0", "C1", "D1", "E1", "F1", "G1", "A1", "B1","C2", "D2", "E2", "F2", "G2", "A2", "B2", "C3", "D3", "E3", "F3", "G3","A3", "B3","C4", "D4", "E4", " AltF4"]
alphabet = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
encoding_map = {alphabet[i] : codeAlphabet[i] for i in range(27)}
decoding_map = {v: k for k, v in encoding_map.items()}
#Encode
if select.lower() == "encode":
    encodeText = input("What text would you like to encode?")
    def encode_text(text):
        text = encodeText.upper()  # Convert to uppercase
        encoded_text = [encoding_map[char] for char in text if char in encoding_map]
        return " ".join(encoded_text)
    pianoShifttext = encode_text(encodeText)
    print(f"Coded version:{pianoShifttext}")
    print("Thank you for using me!")
#Decode
elif select.lower() == "decode":
    message = input("What text would you like to decode?")
    def decode_text(text):
        notes = text.split()
        decoded_text = []
        for note in notes:
            if note in decoding_map:
                decoded_text.append(decoding_map[note])
            else:
                decoded_text.append(note) #Keep notes if not in decoding map
        return "".join(decoded_text)
    decoded_message = decode_text(message)
    print(decoded_message)
    print("Thank You For using me")
else:
    print("Please enter a valid answer")
quit()
