from json import loads

from linepy import *
from Secret import *

line = LINE(line_token)
line.log(line.authToken)
oepoll = OEPoll(line)


def receive_message(operation):  # Type: 26
    try:
        msg = operation.message
        text = msg.text
        msg_id = msg.id
        receiver = msg.to
        sender = msg._from
        sender_name = line.getContact(sender).displayName
        file_name = str(operation.revision)
        content_list = [0, 1, 2, 3, 4, 6, 7, 12, 13, 14, 16, 18]
        if msg.toType == 0:
            # line.sendChatChecked(sender, msg_id)
            if msg.contentType not in content_list:
                print("contentType: " + str(msg.contentType))
                print(operation)
            else:
                action(msg, text, sender, sender_name, msg_id, file_name, 'ME')
        elif msg.toType == 2:
            # line.sendChatChecked(receiver, msg_id)
            group_name = line.getGroup(receiver).name
            if msg.contentType not in content_list:
                print("contentType: " + str(msg.contentType))
                print(operation)
            else:
                action(msg, text, receiver, sender_name, msg_id, file_name, group_name)
    except Exception as e:
        line.log(COLOR.FAIL + "[RECEIVE_MESSAGE]" + COLOR.END + " ERROR : " + str(e))


def action(msg, text, sender, sender_name, msg_id, file_name, group_name):
    try:
        if msg.contentType == 0:
            context(msg, text, sender_name, group_name)
        elif msg.contentType == 1:
            photo(msg, sender_name, msg_id, file_name, group_name)
        elif msg.contentType == 2:
            video(sender_name, msg_id, file_name, group_name)
        elif msg.contentType == 3:
            audio(sender_name, msg_id, file_name, group_name)
        elif msg.contentType == 4:
            ladder_shuffle()
        elif msg.contentType == 6:
            call()
        elif msg.contentType == 7:
            sticker(msg, sender_name, group_name)
        elif msg.contentType == 12:
            event()
        elif msg.contentType == 13:
            contact(msg, sender_name, group_name)
        elif msg.contentType == 14:
            file(msg, sender_name, msg_id, group_name)
        elif msg.contentType == 16:
            notification(msg, sender_name, group_name)
        elif msg.contentType == 18:
            delete_photo_in_album(msg, sender_name, group_name)
        else:
            line.log("[UNKNOWN_CONTENT_TYPE]")
    except Exception as e:
        line.log(COLOR.FAIL + "[ACTION]" + COLOR.END + " ERROR : " + str(e))


def context(msg, text, sender_name, group_name):
    try:
        if msg.location is not None:
            line.log(
                COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                ' sent a location: %s' % str(msg.location))
        elif msg.relatedMessageId is not None:
            line.log(COLOR.FAIL + '[HANDLE_MESSAGE_ERROR]: %s' % msg + COLOR.END)
        else:
            line.log(
                COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                ' %s' % text)
    except Exception as e:
        line.log(COLOR.FAIL + "[CONTEXT]" + COLOR.END + " ERROR : " + str(e))


def photo(msg, sender_name, msg_id, file_name, group_name):
    try:
        if 'MEDIA_CONTENT_INFO' in msg.contentMetadata:
            extension = loads(msg.contentMetadata['MEDIA_CONTENT_INFO'])['extension']
            if extension == 'png':
                line.downloadObjectMsg(msg_id, saveAs=save_path + file_name + '.png')
                line.log(
                    COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                    ' sent a PNG: %s' % file_name + '.png')
            elif extension == 'JPEG':
                line.downloadObjectMsg(msg_id, saveAs=save_path + file_name + '.jpg')
                line.log(
                    COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                    ' sent a JPEG: %s' % file_name + '.jpg')
            elif extension == 'gif':
                line.downloadObjectMsg(msg_id, saveAs=save_path + file_name + '.gif')
                line.log(
                    COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                    ' sent a GIF: %s' % file_name + '.gif')
            else:
                print(msg)
        else:
            line.downloadObjectMsg(msg_id, saveAs=save_path + file_name + '.jpg')
            line.log(
                COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                ' sent a picture: %s' % file_name + '.jpg')
    except Exception as e:
        line.log(COLOR.FAIL + "[PHOTO]" + COLOR.END + " ERROR : " + str(e))


def video(sender_name, msg_id, file_name, group_name):
    try:
        line.downloadObjectMsg(msg_id, saveAs=save_path + file_name + '.mp4')
        line.log(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
            ' sent a video: %s' % file_name)
    except Exception as e:
        line.log(COLOR.FAIL + "[VIDEO]" + COLOR.END + " ERROR : " + str(e) + "\nMessage ID is: " + msg_id)


def audio(sender_name, msg_id, file_name, group_name):
    try:
        line.downloadObjectMsg(msg_id, saveAs=save_path + file_name + '.mp4')
        line.log(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
            ' sent an audio message: %s' % file_name + '.mp4')
    except Exception as e:
        line.log(COLOR.FAIL + "[AUDIO]" + COLOR.END + " ERROR : " + str(e))


def ladder_shuffle():
    try:
        print('ladder_shuffle')
    except Exception as e:
        line.log(COLOR.FAIL + "[LADDER_SHUFFLE]" + COLOR.END + " ERROR : " + str(e))


def call():
    try:
        print('call')
    except Exception as e:
        line.log(COLOR.FAIL + "[CALL]" + COLOR.END + " ERROR : " + str(e))


def sticker(msg, sender_name, group_name):
    try:
        txt = 'send a sticker\n' + \
              '  Sticker Package ID: %s\n' % str(msg.contentMetadata['STKPKGID']) + \
              '  Sticker ID: %s' % str(msg.contentMetadata['STKID'])
        line.log(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
            ' %s' % txt)
    except Exception as e:
        line.log(COLOR.FAIL + "[STICKER]" + COLOR.END + " ERROR : " + str(e))


def event():
    try:
        print('event')
    except Exception as e:
        line.log(COLOR.FAIL + "[EVENT]" + COLOR.END + " ERROR : " + str(e))


def contact(msg, sender_name, group_name):
    try:
        contact_id = msg.contentMetadata['mid']
        line.log(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
            ' sent contact: %s' % contact_id)
    except Exception as e:
        line.log(COLOR.FAIL + "[CONTACT]" + COLOR.END + " ERROR : " + str(e))


def file(msg, sender_name, msg_id, group_name):
    try:
        file_name = str(msg.contentMetadata['FILE_NAME'])
        line.downloadObjectMsg(msg_id, saveAs=save_path + file_name)
        line.log(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
            ' sent a file: %s' % file_name)
    except Exception as e:
        line.log(COLOR.FAIL + "[FILE]" + COLOR.END + " ERROR : " + str(e))


def notification(msg, sender_name, group_name):
    lockey = msg.contentMetadata['locKey']
    if lockey == 'BN':
        line.log(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '@ %s' % group_name + COLOR.END +
            ' sent a note.')
    elif lockey == 'BA':
        line.log(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '@ %s' % group_name + COLOR.END +
            ' created an album: %s, photos: (%s+1)' % (
                msg.contentMetadata['albumName'], msg.contentMetadata['mediaCount']))
    elif lockey == 'BT':
        line.log(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '@ %s' % group_name + COLOR.END +
            ' add photos (%s+1) in an album: %s' % (
                msg.contentMetadata['mediaCount'], msg.contentMetadata['albumName']))
    else:
        print(msg)


def delete_photo_in_album(msg, sender_name, group_name):
    loc_key = msg.contentMetadata['LOC_KEY']
    album_name = msg.contentMetadata['LOC_ARGS']
    if loc_key == 'BO':
        line.log(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
            ' delete photo in %s' % album_name)
    elif loc_key == 'BD':
        line.log(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
            ' delete album: %s' % album_name)


oepoll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: receive_message
})

if __name__ == '__main__':
    while True:
        oepoll.trace()
