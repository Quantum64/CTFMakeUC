import base64

data = b"f0VMRgEBAQAAAAAAAAAAAAIAAwABAAAAYIcECDQAAADQHQAAAAAAADQAIAAIACgAHQAcAAYAAAA0AAAANIAECDSABAgAAQAAAAEAAAUAAAAEAAAAAwAAADQBAAA0gQQINIEECBMAAAATAAAABAAAAAEAAAABAAAAAAAAAACABAgAgAQINBsAADQbAAAFAAAAABAAAAEAAAA0GwAANKsECDSrBAhsAQAAeAEAAAYAAAAAEAAAAgAAAEAbAABAqwQIQKsECOgAAADoAAAABgAAAAQAAAAEAAAASAEAAEiBBAhIgQQIRAAAAEQAAAAEAAAABAAAAFDldGREGAAARJgECESYBAiMAAAAjAAAAAQAAAAEAAAAUeV0ZAAAAAAAAAAAAAAAAAAAAAAAAAAABwAAABAAAAAvbGliL2xkLWxpbnV4LnNvLjIAAAQAAAAQAAAAAQAAAEdOVQAAAAAAAgAAAAYAAAAgAAAABAAAABQAAAADAAAAR05VAMAtIoBiE07tybRPUKaTSvXLsUqiAgAAABoAAAABAAAABQAAAAAjACAaAAAAGwAAACkdjBytS+PAAAAAAAAAAAAAAAAAAAAAAEYAAAAAAAAAAAAAABIAAABdAAAAAAAAAAAAAAASAAAAwAAAAAAAAAAAAAAAEgAAAMcAAAAAAAAAAAAAABIAAABzAAAAAAAAAAAAAAASAAAAOQAAAAAAAAAAAAAAEgAAAIEAAAAAAAAAAAAAABIAAACcAAAAAAAAAAAAAAASAAAAYgAAAAAAAAAAAAAAEgAAAIcAAAAAAAAAAAAAABIAAACOAAAAAAAAAAAAAAASAAAAegAAAAAAAAAAAAAAEgAAAKUAAAAAAAAAAAAAABIAAAA0AAAAAAAAAAAAAAASAAAAzAAAAAAAAAAAAAAAIAAAACEAAAAAAAAAAAAAABIAAABPAAAAAAAAAAAAAAASAAAArAAAAAAAAAAAAAAAEgAAAJQAAAAAAAAAAAAAABIAAAAuAAAAAAAAAAAAAAASAAAAVgAAAAAAAAAAAAAAEgAAAL4AAAAAAAAAAAAAABIAAAA+AAAAAAAAAAAAAAASAAAAGgAAAAAAAAAAAAAAEgAAACYAAAAAAAAAAAAAABIAAABsAAAAoKwECAQAAAARABoACwAAAISUBAgEAAAAEQAQAABsaWJjLnNvLjYAX0lPX3N0ZGluX3VzZWQAc2V0dWlkAGV4aXQAc3ByaW50ZgBmb3BlbgBwdXRzAHRpbWUAcHV0Y2hhcgBnZXRwd25hbQBzdHJsZW4AbWVtc2V0AHJlYWQAc2V0Z3JvdXBzAHN0ZG91dABmY2xvc2UAbWFsbG9jAGFsYXJtAGZ3cml0ZQBiY29weQBzZXR2YnVmAF9JT19nZXRjAHNldGdpZABfX2xpYmNfc3RhcnRfbWFpbgBzbnByaW50ZgBmcmVlAF9fZ21vbl9zdGFydF9fAEdMSUJDXzIuMQBHTElCQ18yLjAAAAAAAgACAAIAAgADAAIAAgACAAIAAgACAAIAAgACAAAAAgACAAIAAgADAAIAAgACAAIAAgACAAEAAQACAAEAAAAQAAAAAAAAABFpaQ0AAAMA2wAAABAAAAAQaWkNAAACAOUAAAAAAAAAKKwECAYPAACgrAQIBRoAADisBAgHAQAAPKwECAcCAABArAQIBwMAAESsBAgHBAAASKwECAcFAABMrAQIBwYAAFCsBAgHBwAAVKwECAcIAABYrAQIBwkAAFysBAgHCgAAYKwECAcLAABkrAQIBwwAAGisBAgHDQAAbKwECAcOAABwrAQIBxAAAHSsBAgHEQAAeKwECAcSAAB8rAQIBxMAAICsBAgHFAAAhKwECAcVAACIrAQIBxYAAIysBAgHFwAAkKwECAcYAACUrAQIBxkAAFOD7Ajo7wEAAIHDiyYAAIuD/P///4XAdAXomgEAAIPECFvDAAAAAAD/NTCsBAj/JTSsBAgAAAAA/yU4rAQIaAAAAADp4P////8lPKwECGgIAAAA6dD/////JUCsBAhoEAAAAOnA/////yVErAQIaBgAAADpsP////8lSKwECGggAAAA6aD/////JUysBAhoKAAAAOmQ/////yVQrAQIaDAAAADpgP////8lVKwECGg4AAAA6XD/////JVisBAhoQAAAAOlg/////yVcrAQIaEgAAADpUP////8lYKwECGhQAAAA6UD/////JWSsBAhoWAAAAOkw/////yVorAQIaGAAAADpIP////8lbKwECGhoAAAA6RD/////JXCsBAhocAAAAOkA/////yV0rAQIaHgAAADp8P7///8leKwECGiAAAAA6eD+////JXysBAhoiAAAAOnQ/v///yWArAQIaJAAAADpwP7///8lhKwECGiY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"

with open("blob.bin", "wb") as fh:
    fh.write(base64.decodebytes(data))