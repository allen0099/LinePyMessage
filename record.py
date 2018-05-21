"""
Auto join the group and print received messages.
"""

from json import loads
from linepy import *
from secret_class import *
from colors import *


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


def end_of_operation(operation):  # Type: 0
    print(operation)


def update_profile(operation):  # Type: 1
    print(operation)


def update_settings(operation):  # Type: 36
    print(operation)


def notified_update_profile(operation):  # Type: 2
    try:
        name = line.getContact(operation.param1).displayName
        if operation.param2 == '2':
            line_print(
                COLOR.NOTIFIED + '[%s]' % name + COLOR.END + ' updated name: %s' % name)
        elif operation.param2 == '16':
            status = line.getContact(operation.param1).statusMessage
            line_print(
                COLOR.NOTIFIED + '[%s]' % name + COLOR.END + ' updated status: %s' % status)
        else:
            print(operation.param2)
        print(operation.param3)
    except Exception as e:
        line_print(COLOR.FAIL + "[UPDATE_PROFILE]" + COLOR.END + " ERROR : " + str(e))


# noinspection SpellCheckingInspection
def register_userid(operation):  # Type: 3
    print(operation)


def add_contact(operation):  # Type: 4
    print(operation)


def notified_add_contact(operation):  # Type: 5
    print(operation)


def block_contact(operation):  # Type: 6
    print(operation)


def unblock_contact(operation):  # Type: 7
    print(operation)


def notified_recommend_contact(operation):  # Type: 8
    print(operation)


def create_group(operation):  # Type: 9
    print(operation)


def update_group(operation):  # Type: 10
    try:
        group_name = line.getGroup(operation.param1).name
        if operation.param2 == '1':
            line_print(
                COLOR.NOTIFIED + '{%s}' % group_name + COLOR.END + ' updated group name')
        elif operation.param2 == '2':
            line_print(
                COLOR.NOTIFIED + '{%s}' % group_name + COLOR.END + ' updated group photo')
        elif operation.param2 == '4':
            line_print(
                COLOR.NOTIFIED + '{%s}' % group_name + COLOR.END + ' updated invite by link or qr code')
        else:
            print(operation)
    except Exception as e:
        line_print(COLOR.FAIL + "[UPDATE_GROUP]" + COLOR.END + " ERROR : " + str(e))


def notified_update_group(operation):  # Type: 11
    print(operation)


def invite_into_group(operation):  # Type: 12
    print(operation)


def notified_invite_into_group(operation):  # Type: 13
    try:
        # TODO: 這個應該是邀請而不是加入群組
        print(operation)
        group_id = operation.param1
        group_name = line.getGroup(group_id).name
        # auto accept join group
        line.acceptGroupInvitation(group_id)
        line_print(COLOR.WARNING + 'Joined a group: %s' % group_name + COLOR.END)
    except Exception as e:
        line_print(COLOR.FAIL + "[NOTIFIED_INVITE_INTO_GROUP]" + COLOR.END + " ERROR : " + str(e))


def cancel_invitation_group(operation):  # Type: 31
    print(operation)


def notified_cancel_invitation_group(operation):  # Type: 32
    print(operation)


def leave_group(operation):  # Type: 14
    print(operation)


def notified_leave_group(operation):  # Type: 15
    print(operation)


def accept_group_invitation(operation):  # Type: 16
    print(operation)


def notified_accept_group_invitation(operation):  # Type: 17
    try:
        group_id = operation.param1
        user_id = operation.param2
        group_name = line.getGroup(group_id).name
        user_name = line.getContact(user_id).displayName
        line_print(
            COLOR.NOTIFIED + '[%s]' % user_name + COLOR.END +
            ' accepted to join the group: ' + COLOR.BOLD + '%s' % group_name + COLOR.END)
    except Exception as e:
        line_print(COLOR.FAIL + "[NOTIFIED_LEAVE_GROUP]" + COLOR.END + " ERROR : " + str(e))


def reject_group_invitation(operation):  # Type: 34
    print(operation)


def notified_reject_group_invitation(operation):  # Type: 35
    print(operation)


# noinspection SpellCheckingInspection
def kickout_from_group(operation):  # Type: 18
    try:
        group = line.getGroup(operation.param1).name
        kicked = line.getContact(operation.param2).displayName
        line_print(
            COLOR.RED + '[%s]' % kicked + COLOR.END + ' in ' + COLOR.BOLD + '{%s}' % group + COLOR.END +
            ' has been kicked by ' + COLOR.RED + 'ME' + COLOR.END)
    except Exception as e:
        line_print(COLOR.FAIL + "[KICKOUT_FROM_GROUP]" + COLOR.END + " ERROR : " + str(e))


# noinspection SpellCheckingInspection
def notified_kickout_from_group(operation):  # Type: 19
    try:
        group_name = line.getGroup(operation.param1).name
        user_kick_other = line.getContact(operation.param2).displayName
        user_kicked = line.getContact(operation.param3).displayName
        line_print(
            COLOR.RED + '[%s]' % user_kicked + COLOR.END + ' in ' + COLOR.BOLD + '{%s}' % group_name + COLOR.END +
            ' has been kicked by ' + COLOR.RED + '%s' % user_kick_other)
    except Exception as e:
        line_print(COLOR.FAIL + "[NOTIFIED_KICKOUT_FROM_GROUP]" + COLOR.END + " ERROR : " + str(e))


def create_room(operation):  # Type: 20
    print(operation)


def invite_into_room(operation):  # Type: 21
    print(operation)


def notified_invite_into_room(operation):  # Type: 22
    print(operation)


def leave_room(operation):  # Type: 23
    print(operation)


def notified_leave_room(operation):  # Type: 24
    print(operation)


def send_message(operation):  # Type: 25
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
        line_print(COLOR.FAIL + "[SEND_MESSAGE]" + COLOR.END + " ERROR : " + str(e))


def send_message_receipt(operation):  # Type: 27
    print(operation)


def receive_message_receipt(operation):  # Type: 28
    print(operation)


def send_content_receipt(operation):  # Type: 29
    print(operation)


def receive_announcement(operation):  # Type: 30
    print(operation)


def notified_unregister_user(operation):  # Type: 33
    print(operation)


def invite_via_email(operation):  # Type: 38
    print(operation)


def notified_register_user(operation):  # Type: 37
    print(operation)


def notified_request_recovery(operation):  # Type: 39
    print(operation)


def send_chat_checked(operation):  # Type: 40
    print(operation)


def send_chat_removed(operation):  # Type: 41
    print(operation)


def notified_force_sync(operation):  # Type: 42
    print(operation)


def send_content(operation):  # Type: 43
    print(operation)


# noinspection SpellCheckingInspection
def send_message_myhome(operation):  # Type: 44
    print(operation)


def notified_update_content_preview(operation):  # Type: 45
    print(operation)


def remove_all_messages(operation):  # Type: 46
    print(operation)


def notified_update_purchases(operation):  # Type: 47
    print(operation)


def dummy(operation):  # Type: 48
    print(operation)


def update_contact(operation):  # Type: 49
    print(operation)


def notified_received_call(operation):  # Type: 50
    print(operation)


def cancel_call(operation):  # Type: 51
    print(operation)


def notified_redirect(operation):  # Type: 52
    print(operation)


def notified_channel_sync(operation):  # Type: 53
    print(operation)


def failed_send_message(operation):  # Type: 54
    print(operation)


def notified_read_message(operation):  # Type: 55
    try:
        name = ''
        if operation.param1.startswith('u'):
            name = line.getContact(operation.param1).displayName
        elif operation.param1.startswith('c'):
            name = line.getGroup(operation.param1).name
        else:
            print(operation.param1)
        reader = line.getContact(operation.param2).displayName
        line_print(
            COLOR.READ + '[%s] ' % reader + COLOR.BOLD + '@{%s}' % name + COLOR.END +
            ' read the message.')
    except Exception as e:
        line_print(COLOR.FAIL + "[NOTIFIED_READ_MESSAGE]" + COLOR.END + " ERROR : " + str(e))


def failed_email_confirmation(operation):  # Type: 56
    print(operation)


def notified_chat_content(operation):  # Type: 58
    print(operation)


# noinspection SpellCheckingInspection
def notified_push_noticenter_item(operation):  # Type: 59
    print(operation)


def notified_join_chat(operation):  # Type: 60
    try:
        group_id = operation.param1
        joiner_id = operation.param2
        group_name = line.getGroup(group_id).name
        joiner_name = line.getContact(joiner_id).displayName
        line_print(
            COLOR.NOTIFIED + '[%s]' % joiner_name + COLOR.END +
            ' has joined the group: ' + COLOR.BOLD + '%s' % group_name + COLOR.END)
    except Exception as e:
        line_print(COLOR.FAIL + "[NOTIFIED_JOIN_CHAT]" + COLOR.END + " ERROR : " + str(e))


def notified_leave_chat(operation):  # Type: 61
    try:
        group = line.getGroup(operation.param1).name
        leaver = line.getContact(operation.param2).displayName
        line_print(
            COLOR.NOTIFIED + '[%s]' % leaver + COLOR.END +
            ' has left the group: ' + COLOR.BOLD + '%s' % group + COLOR.END)
    except Exception as e:
        line_print(COLOR.FAIL + "[NOTIFIED_LEAVE_CHAT]" + COLOR.END + " ERROR : " + str(e))


def notified_typing(operation):  # Type: 62
    print(operation)


def friend_request_accepted(operation):  # Type: 63
    print(operation)


def destroy_message(operation):  # Type: 64
    try:
        name = ''
        if operation.param1.startswith('u'):
            name = line.getContact(operation.param1).displayName
        elif operation.param1.startswith('c'):
            name = line.getGroup(operation.param1).name
        else:
            print(operation.param1)
        msg_id = operation.param2
        line_print(
            COLOR.WARNING + '{%s}' % name + COLOR.END + ' unsent the message: %s' % msg_id)
    except Exception as e:
        line_print(COLOR.FAIL + "[DESTROY_MESSAGE]" + COLOR.END + " ERROR : " + str(e))


def notified_destroy_message(operation):  # Type: 65
    try:
        name = ''
        if operation.param1.startswith('u'):
            name = line.getContact(operation.param1).displayName
        elif operation.param1.startswith('c'):
            name = line.getGroup(operation.param1).name
        else:
            print(operation.param1)
        msg_id = operation.param2
        line_print(
            COLOR.WARNING + '{%s}' % name + COLOR.END + ' unsent the message: %s' % msg_id)
    except Exception as e:
        line_print(COLOR.FAIL + "[DESTROY_MESSAGE]" + COLOR.END + " ERROR : " + str(e))


# noinspection SpellCheckingInspection
def update_publickeychain(operation):  # Type: 66
    print(operation)


# noinspection SpellCheckingInspection
def notified_update_publickeychain(operation):  # Type: 67
    print(operation)


def notified_block_contact(operation):  # Type: 68
    print(operation)


def notified_unblock_contact(operation):  # Type: 69
    print(operation)


# noinspection SpellCheckingInspection
def update_grouppreference(operation):  # Type: 70
    print(operation)


def notified_payment_event(operation):  # Type: 71
    print(operation)


# noinspection SpellCheckingInspection
def register_e2ee_publickey(operation):  # Type: 72
    print(operation)


def notified_e2ee_key_exchange_req(operation):  # Type: 73
    print(operation)


def notified_e2ee_key_exchange_resp(operation):  # Type: 74
    print(operation)


def notified_e2ee_message_resend_req(operation):  # Type: 75
    print(operation)


def notified_e2ee_message_resend_resp(operation):  # Type: 76
    print(operation)


def notified_e2ee_key_update(operation):  # Type: 77
    print(operation)


def notified_buddy_update_profile(operation):  # Type: 78
    print(operation)


# noinspection SpellCheckingInspection
def notified_update_lineat_labs(operation):  # Type: 79
    print(operation)


def update_room(operation):  # Type: 80
    print(operation)


def notified_beacon_detected(operation):  # Type: 81
    print(operation)


def update_extended_profile(operation):  # Type: 82
    print(operation)


def add_follow(operation):  # Type: 83
    print(operation)


def notified_add_follow(operation):  # Type: 84
    print(operation)


def delete_follow(operation):  # Type: 85
    print(operation)


def notified_delete_follow(operation):  # Type: 86
    print(operation)


# noinspection SpellCheckingInspection
def update_timeline_settings(operation):  # Type: 87
    print(operation)


def notified_friend_request(operation):  # Type: 88
    print(operation)


# noinspection SpellCheckingInspection
def update_ringback_tone(operation):  # Type: 89
    print(operation)


# noinspection SpellCheckingInspection
def notified_postback(operation):  # Type: 90
    print(operation)


def receive_read_watermark(operation):  # Type: 91
    print(operation)


def notified_message_delivered(operation):  # Type: 92
    print(operation)


def notified_update_chat_bar(operation):  # Type: 93
    print(operation)


# noinspection SpellCheckingInspection
def notified_chatapp_installed(operation):  # Type: 94
    print(operation)


# noinspection SpellCheckingInspection
def notified_chatapp_updated(operation):  # Type: 95
    print(operation)


def notified_chat_app_new_mark(operation):  # Type: 96
    print(operation)


# noinspection SpellCheckingInspection
def notified_chatapp_deleted(operation):  # Type: 97
    print(operation)


# noinspection SpellCheckingInspection
def notified_chatapp_sync(operation):  # Type: 98
    print(operation)


def notified_update_message(operation):  # Type: 99
    print(operation)


if __name__ == '__main__':
    line = LINE(line_token)
    line_print(line.authToken)
    oepoll = OEPoll(line)

    oepoll.addOpInterruptWithDict({
        OpType.END_OF_OPERATION: end_of_operation,
        OpType.UPDATE_PROFILE: update_profile,
        OpType.UPDATE_SETTINGS: update_settings,
        OpType.NOTIFIED_UPDATE_PROFILE: notified_update_profile,
        OpType.REGISTER_USERID: register_userid,
        OpType.ADD_CONTACT: add_contact,
        OpType.NOTIFIED_ADD_CONTACT: notified_add_contact,
        OpType.BLOCK_CONTACT: block_contact,
        OpType.UNBLOCK_CONTACT: unblock_contact,
        OpType.NOTIFIED_RECOMMEND_CONTACT: notified_recommend_contact,
        OpType.CREATE_GROUP: create_group,
        OpType.UPDATE_GROUP: update_group,
        OpType.NOTIFIED_UPDATE_GROUP: notified_update_group,
        OpType.INVITE_INTO_GROUP: invite_into_group,
        OpType.NOTIFIED_INVITE_INTO_GROUP: notified_invite_into_group,
        OpType.CANCEL_INVITATION_GROUP: cancel_invitation_group,
        OpType.NOTIFIED_CANCEL_INVITATION_GROUP: notified_cancel_invitation_group,
        OpType.LEAVE_GROUP: leave_group,
        OpType.NOTIFIED_LEAVE_GROUP: notified_leave_group,
        OpType.ACCEPT_GROUP_INVITATION: accept_group_invitation,
        OpType.NOTIFIED_ACCEPT_GROUP_INVITATION: notified_accept_group_invitation,
        OpType.REJECT_GROUP_INVITATION: reject_group_invitation,
        OpType.NOTIFIED_REJECT_GROUP_INVITATION: notified_reject_group_invitation,
        OpType.KICKOUT_FROM_GROUP: kickout_from_group,
        OpType.NOTIFIED_KICKOUT_FROM_GROUP: notified_kickout_from_group,
        OpType.CREATE_ROOM: create_room,
        OpType.INVITE_INTO_ROOM: invite_into_room,
        OpType.NOTIFIED_INVITE_INTO_ROOM: notified_invite_into_room,
        OpType.LEAVE_ROOM: leave_room,
        OpType.NOTIFIED_LEAVE_ROOM: notified_leave_room,
        OpType.SEND_MESSAGE: send_message,
        OpType.RECEIVE_MESSAGE: receive_message,
        OpType.SEND_MESSAGE_RECEIPT: send_message_receipt,
        OpType.RECEIVE_MESSAGE_RECEIPT: receive_message_receipt,
        OpType.SEND_CONTENT_RECEIPT: send_content_receipt,
        OpType.RECEIVE_ANNOUNCEMENT: receive_announcement,
        OpType.NOTIFIED_UNREGISTER_USER: notified_unregister_user,
        OpType.INVITE_VIA_EMAIL: invite_via_email,
        OpType.NOTIFIED_REGISTER_USER: notified_register_user,
        OpType.NOTIFIED_REQUEST_RECOVERY: notified_request_recovery,
        # OpType.SEND_CHAT_CHECKED: send_chat_checked,
        OpType.SEND_CHAT_REMOVED: send_chat_removed,
        OpType.NOTIFIED_FORCE_SYNC: notified_force_sync,
        OpType.SEND_CONTENT: send_content,
        OpType.SEND_MESSAGE_MYHOME: send_message_myhome,
        OpType.NOTIFIED_UPDATE_CONTENT_PREVIEW: notified_update_content_preview,
        OpType.REMOVE_ALL_MESSAGES: remove_all_messages,
        OpType.NOTIFIED_UPDATE_PURCHASES: notified_update_purchases,
        # OpType.DUMMY: dummy,
        OpType.UPDATE_CONTACT: update_contact,
        OpType.NOTIFIED_RECEIVED_CALL: notified_received_call,
        OpType.CANCEL_CALL: cancel_call,
        OpType.NOTIFIED_REDIRECT: notified_redirect,
        OpType.NOTIFIED_CHANNEL_SYNC: notified_channel_sync,
        OpType.FAILED_SEND_MESSAGE: failed_send_message,
        OpType.NOTIFIED_READ_MESSAGE: notified_read_message,
        OpType.FAILED_EMAIL_CONFIRMATION: failed_email_confirmation,
        OpType.NOTIFIED_CHAT_CONTENT: notified_chat_content,
        OpType.NOTIFIED_PUSH_NOTICENTER_ITEM: notified_push_noticenter_item,
        OpType.NOTIFIED_JOIN_CHAT: notified_join_chat,
        OpType.NOTIFIED_LEAVE_CHAT: notified_leave_chat,
        OpType.NOTIFIED_TYPING: notified_typing,
        OpType.FRIEND_REQUEST_ACCEPTED: friend_request_accepted,
        OpType.DESTROY_MESSAGE: destroy_message,
        OpType.NOTIFIED_DESTROY_MESSAGE: notified_destroy_message,
        OpType.UPDATE_PUBLICKEYCHAIN: update_publickeychain,
        OpType.NOTIFIED_UPDATE_PUBLICKEYCHAIN: notified_update_publickeychain,
        OpType.NOTIFIED_BLOCK_CONTACT: notified_block_contact,
        OpType.NOTIFIED_UNBLOCK_CONTACT: notified_unblock_contact,
        OpType.UPDATE_GROUPPREFERENCE: update_grouppreference,
        OpType.NOTIFIED_PAYMENT_EVENT: notified_payment_event,
        OpType.REGISTER_E2EE_PUBLICKEY: register_e2ee_publickey,
        OpType.NOTIFIED_E2EE_KEY_EXCHANGE_REQ: notified_e2ee_key_exchange_req,
        OpType.NOTIFIED_E2EE_KEY_EXCHANGE_RESP: notified_e2ee_key_exchange_resp,
        OpType.NOTIFIED_E2EE_MESSAGE_RESEND_REQ: notified_e2ee_message_resend_req,
        OpType.NOTIFIED_E2EE_MESSAGE_RESEND_RESP: notified_e2ee_message_resend_resp,
        OpType.NOTIFIED_E2EE_KEY_UPDATE: notified_e2ee_key_update,
        OpType.NOTIFIED_BUDDY_UPDATE_PROFILE: notified_buddy_update_profile,
        OpType.NOTIFIED_UPDATE_LINEAT_TABS: notified_update_lineat_labs,
        OpType.UPDATE_ROOM: update_room,
        OpType.NOTIFIED_BEACON_DETECTED: notified_beacon_detected,
        OpType.UPDATE_EXTENDED_PROFILE: update_extended_profile,
        OpType.ADD_FOLLOW: add_follow,
        OpType.NOTIFIED_ADD_FOLLOW: notified_add_follow,
        OpType.DELETE_FOLLOW: delete_follow,
        OpType.NOTIFIED_DELETE_FOLLOW: notified_delete_follow,
        OpType.UPDATE_TIMELINE_SETTINGS: update_timeline_settings,
        OpType.NOTIFIED_FRIEND_REQUEST: notified_friend_request,
        OpType.UPDATE_RINGBACK_TONE: update_ringback_tone,
        OpType.NOTIFIED_POSTBACK: notified_postback,
        OpType.RECEIVE_READ_WATERMARK: receive_read_watermark,
        OpType.NOTIFIED_MESSAGE_DELIVERED: notified_message_delivered,
        OpType.NOTIFIED_UPDATE_CHAT_BAR: notified_update_chat_bar,
        OpType.NOTIFIED_CHATAPP_INSTALLED: notified_chatapp_installed,
        OpType.NOTIFIED_CHATAPP_UPDATED: notified_chatapp_updated,
        OpType.NOTIFIED_CHATAPP_NEW_MARK: notified_chat_app_new_mark,
        OpType.NOTIFIED_CHATAPP_DELETED: notified_chatapp_deleted,
        OpType.NOTIFIED_CHATAPP_SYNC: notified_chatapp_sync,
        OpType.NOTIFIED_UPDATE_MESSAGE: notified_update_message
    })

    while True:
        oepoll.trace()
