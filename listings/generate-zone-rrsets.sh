    #!/bin/bash
    for i in $(seq 1 2000); do

        http http://IP:9001/v2/zones/ZONE_ID/recordsets name=ww$i.largetestzone.tld. records:='["10.0.0.1"]' type=A

        http http://IP:9001/v2/zones/ZONE_ID/recordsets name=txt$i.largetestzone.tld. records:='["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam molestie leo sit amet commodo aliquet. Sed semper felis sit amet egestas euismod. Nulla non elementum orci. Nulla pharetra, ligula eget aliquet sagittis, velit nisl rhoncus nibh, vitae amet.", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam molestie leo sit amet commodo aliquet. Sed semper felis sit amet egestas euismod. Nulla non elementum orci. Nulla pharetra, ligula eget aliquet sagittis, velit nisl rhoncus nibh, vitae amet.", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam molestie leo sit amet commodo aliquet. Sed semper felis sit amet egestas euismod. Nulla non elementum orci. Nulla pharetra, ligula eget aliquet sagittis, velit nisl rhoncus nibh, vitae amet.", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam molestie leo sit amet commodo aliquet. Sed semper felis sit amet egestas euismod. Nulla non elementum orci. Nulla pharetra, ligula eget aliquet sagittis, velit nisl rhoncus nibh, vitae amet."]' type=TXT
    done
