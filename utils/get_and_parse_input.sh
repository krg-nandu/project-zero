arecord -D plughw:0,0 -t wav -d 3 -r 16000 | flac - -f --best -o /dev/shm/out.flac 1>/dev/shm/voice.log 2>/dev/shm/voice.log; curl -X POST --data-binary @/dev/shm/out.flac --user-agent 'Mozilla/5.0' --header 'Content-Type: audio/x-flac; rate=16000;' "https://www.google.com/speech-api/v2/recognize?output=json&lang=eng&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw&client=Mozilla/5.0" | sed -e 's/[{}]/''/g' > output.txt #| awk -F":" '{print $4}' | awk -F"," '{print $1}' > tmpf.txt #| tr -d '\n'
rm /dev/shm/out.flac