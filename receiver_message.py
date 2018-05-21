"""It can receive all messages.
It only focus on Type 26 and don't do any response.
"""

from json import loads

from linepy import *
from colors import *
from secret_class import *


def receive_message(operation):  # Type: 26
    try:
        msg = operation.message
        text = msg.text
        msg_id = msg.id
        receiver = msg.to
        # noinspection PyProtectedMember
        sender = msg._from
        sender_name = line.getContact(sender).displayName
        file_name = str(operation.revision)
        content_list = [0, 1, 2, 3, 6, 7, 12, 13, 14, 16, 18]
        if msg.toType == 0:
            # line.sendChatChecked(sender, msg_id)
            if msg.contentType not in content_list:
                print("contentType: " + str(msg.contentType))
                print(operation)
            else:
                action(msg, text, sender_name, msg_id, file_name, 'ME')
        elif msg.toType == 2:
            # line.sendChatChecked(receiver, msg_id)
            group_name = line.getGroup(receiver).name
            if msg.contentType not in content_list:
                print("contentType: " + str(msg.contentType))
                print(operation)
            else:
                action(msg, text, sender_name, msg_id, file_name, group_name)
    except Exception as e:
        line_print(COLOR.FAIL + "[RECEIVE_MESSAGE]" + COLOR.END + " ERROR : " + str(e))


def action(msg, text, sender_name, msg_id, file_name, group_name):
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
            events()
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
            line_print("[UNKNOWN_CONTENT_TYPE]")
    except Exception as e:
        line_print(COLOR.FAIL + "[ACTION]" + COLOR.END + " ERROR : " + str(e))


def context(msg, text, sender_name, group_name):
    try:
        if msg.location is not None:
            line_print(
                COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                ' sent a location: %s' % str(msg.location))
            line_log_to_file(
                '[%s] ' % sender_name + '-> %s' % group_name +
                ' sent a location: %s' % str(msg.location))
        elif msg.relatedMessageId is not None:
            line_print(COLOR.FAIL + '[HANDLE_MESSAGE_ERROR]: %s' % msg + COLOR.END)
            line_log_to_file('[HANDLE_MESSAGE_ERROR]: %s' % msg)
        else:
            line_print(
                COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                ' %s' % text)
            line_log_to_file(
                '[%s] ' % sender_name + '-> %s' % group_name +
                ' %s' % text)
    except Exception as e:
        line_print(COLOR.FAIL + "[CONTEXT]" + COLOR.END + " ERROR : " + str(e))


def photo(msg, sender_name, msg_id, file_name, group_name):
    try:
        if 'MEDIA_CONTENT_INFO' in msg.contentMetadata:
            extension = loads(msg.contentMetadata['MEDIA_CONTENT_INFO'])['extension']
            if extension == 'png':
                line.downloadObjectMsg(msg_id, saveAs=save_path + file_name + '.png')
                line_print(
                    COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                    ' sent a PNG: %s' % file_name + '.png')
                line_log_to_file(
                    '[%s] ' % sender_name + '-> %s' % group_name +
                    ' sent a PNG: %s' % file_name + '.png')
            elif extension == 'JPEG':
                line.downloadObjectMsg(msg_id, saveAs=save_path + file_name + '.jpg')
                line_print(
                    COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                    ' sent a JPEG: %s' % file_name + '.jpg')
                line_log_to_file(
                    '[%s] ' % sender_name + '-> %s' % group_name +
                    ' sent a JPEG: %s' % file_name + '.jpg')
            elif extension == 'gif':
                line.downloadObjectMsg(msg_id, saveAs=save_path + file_name + '.gif')
                line_print(
                    COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                    ' sent a GIF: %s' % file_name + '.gif')
                line_log_to_file(
                    '[%s] ' % sender_name + '-> %s' % group_name +
                    ' sent a GIF: %s' % file_name + '.gif')
            else:
                print(msg)
        else:
            line.downloadObjectMsg(msg_id, saveAs=save_path + file_name + '.jpg')
            line_print(
                COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                ' sent a picture: %s' % file_name + '.jpg')
            line_log_to_file(
                '[%s] ' % sender_name + '-> %s' % group_name +
                ' sent a picture: %s' % file_name + '.jpg')
    except Exception as e:
        line_print(COLOR.FAIL + "[PHOTO]" + COLOR.END + " ERROR : " + str(e))


def video(sender_name, msg_id, file_name, group_name):
    try:
        line.downloadObjectMsg(msg_id, saveAs=save_path + file_name + '.mp4')
        line_print(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
            ' sent a video: %s' % file_name)
        line_log_to_file(
            '[%s] ' % sender_name + '-> %s' % group_name +
            ' sent a video: %s' % file_name)
    except Exception as e:
        line_print(COLOR.FAIL + "[VIDEO]" + COLOR.END + " ERROR : " + str(e) + "\nMessage ID is: " + msg_id)


def audio(sender_name, msg_id, file_name, group_name):
    try:
        line.downloadObjectMsg(msg_id, saveAs=save_path + file_name + '.mp4')
        line_print(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
            ' sent an audio message: %s' % file_name + '.mp4')
        line_log_to_file(
            '[%s] ' % sender_name + '-> %s' % group_name +
            ' sent an audio message: %s' % file_name + '.mp4')
    except Exception as e:
        line_print(COLOR.FAIL + "[AUDIO]" + COLOR.END + " ERROR : " + str(e))


def events():
    try:
        print('event')
    except Exception as e:
        line_print(COLOR.FAIL + "[EVENTS]" + COLOR.END + " ERROR : " + str(e))


def call():
    try:
        print('call')
    except Exception as e:
        line_print(COLOR.FAIL + "[CALL]" + COLOR.END + " ERROR : " + str(e))


# noinspection SpellCheckingInspection
def sticker(msg, sender_name, group_name):
    try:
        txt = 'send a sticker\n' + \
              '  Sticker Package ID: %s\n' % str(msg.contentMetadata['STKPKGID']) + \
              '  Sticker ID: %s' % str(msg.contentMetadata['STKID'])
        line_print(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
            ' %s' % txt)
        line_log_to_file(
            '[%s] ' % sender_name + '-> %s' % group_name +
            ' %s' % txt)
    except Exception as e:
        line_print(COLOR.FAIL + "[STICKER]" + COLOR.END + " ERROR : " + str(e))


def event():
    try:
        print('event')
    except Exception as e:
        line_print(COLOR.FAIL + "[EVENT]" + COLOR.END + " ERROR : " + str(e))


def contact(msg, sender_name, group_name):
    try:
        contact_id = msg.contentMetadata['mid']
        line_print(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
            ' sent contact: %s' % contact_id)
        line_log_to_file(
            '[%s] ' % sender_name + '-> %s' % group_name +
            ' sent contact: %s' % contact_id)
    except Exception as e:
        line_print(COLOR.FAIL + "[CONTACT]" + COLOR.END + " ERROR : " + str(e))


def file(msg, sender_name, msg_id, group_name):
    try:
        file_name = str(msg.contentMetadata['FILE_NAME'])
        line.downloadObjectMsg(msg_id, saveAs=save_path + file_name)
        line_print(
            COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
            ' sent a file: %s' % file_name)
        line_log_to_file(
            '[%s] ' % sender_name + '-> %s' % group_name +
            ' sent a file: %s' % file_name)
    except Exception as e:
        line_print(COLOR.FAIL + "[FILE]" + COLOR.END + " ERROR : " + str(e))


# noinspection SpellCheckingInspection
def notification(msg, sender_name, group_name):
    try:
        lockey = msg.contentMetadata['locKey']
        if lockey == 'BN':
            line_print(
                COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '@ %s' % group_name + COLOR.END +
                ' sent a note.')
            line_log_to_file(
                '[%s] ' % sender_name + '@ %s' % group_name +
                ' sent a note.')
        elif lockey == 'BA':
            line_print(
                COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '@ %s' % group_name + COLOR.END +
                ' created an album: %s, photos: (%s+1)' % (
                    msg.contentMetadata['albumName'], msg.contentMetadata['mediaCount']))
            line_log_to_file(
                '[%s] ' % sender_name + '@ %s' % group_name +
                ' created an album: %s, photos: (%s+1)' % (
                    msg.contentMetadata['albumName'], msg.contentMetadata['mediaCount']))
        elif lockey == 'BT':
            line_print(
                COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '@ %s' % group_name + COLOR.END +
                ' add photos (%s+1) in an album: %s' % (
                    msg.contentMetadata['mediaCount'], msg.contentMetadata['albumName']))
            line_log_to_file(
                '[%s] ' % sender_name + '@ %s' % group_name +
                ' add photos (%s+1) in an album: %s' % (
                    msg.contentMetadata['mediaCount'], msg.contentMetadata['albumName']))
        else:
            print(msg)
    except Exception as e:
        line_print(COLOR.FAIL + "[NOTIFICATION]" + COLOR.END + " ERROR : " + str(e))


def delete_photo_in_album(msg, sender_name, group_name):
    try:
        loc_key = msg.contentMetadata['LOC_KEY']
        album_name = msg.contentMetadata['LOC_ARGS']
        if loc_key == 'BO':
            line_print(
                COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                ' delete photo in %s' % album_name)
            line_log_to_file(
                '[%s] ' % sender_name + '-> %s' % group_name +
                ' delete photo in %s' % album_name)
        elif loc_key == 'BD':
            line_print(
                COLOR.SENDER + '[%s] ' % sender_name + COLOR.BOLD + '-> %s' % group_name + COLOR.END +
                ' delete album: %s' % album_name)
            line_log_to_file(
                '[%s] ' % sender_name + '-> %s' % group_name +
                ' delete album: %s' % album_name)
    except Exception as e:
        line_print(COLOR.FAIL + "[DELETE_PHOTO_IN_ALBUM]" + COLOR.END + " ERROR : " + str(e))


if __name__ == '__main__':
    line = LINE(line_token)
    line.log(line.authToken)
    oepoll = OEPoll(line)

    oepoll.addOpInterruptWithDict({
        OpType.RECEIVE_MESSAGE: receive_message
    })
    while True:
        oepoll.trace()
