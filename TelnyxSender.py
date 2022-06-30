import time
import telnyx
print("- Telegram: @ZoxTn")
Telegram: @ZoxTn
f=raw_input('PhoneNumbers List:')
with open(f) as file1:
Lines = file1.readlines()
count = 0
for line in Lines:
    count += 1
    if (count % 6)== 0:
        time.sleep(61)
    else:
        try:
            telnyx.api_key = "##YOUR-API##"
            destination_number = line
            print(destination_number,"___________....Sent")
            telnyx.Message.create(
                from_="##SENDER-NAME##",
                to=destination_number,
                text="##YOUR-MESSAGE##",
                messaging_profile_id="##PROFILE-ID##",
    )
        except:
            destination_number = line
            print(destination_number,"___________....Error")