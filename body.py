import requests
import json

url = "https://openapi.akool.com/api/open/v3/faceswap/highquality/specifyvideo"

payload = json.dumps({
  "sourceImage": [
    {
      "path": "https://d21ksh0k4smeql.cloudfront.net/crop_1705475757658-3362-0-1705475757797-3713.png",
      "opts": "239,364:386,366:317,472:266,539"
    }
  ],
  "targetImage": [
    {
      "path": "https://d21ksh0k4smeql.cloudfront.net/crop_1705479323786-0321-0-1705479323896-7695.png",
      "opts": "176,259:243,259:209,303:183,328"
    }
  ],
 "face_enhance": 0,
  "modifyVideo": "https://d21ksh0k4smeql.cloudfront.net/avatar_01-1705479314627-0092.mp4",
  "webhookUrl": "http://localhost:3007/api/webhook2"
})
headers = {
  'Authorization': 'Bearer token',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)