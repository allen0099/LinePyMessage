from linepy import *
from secret_class import *

line = LINE(line_token)
oepoll = OEPoll(line)


def receive_message(operation):  # Type: 26
    print(operation)


def end_of_operation(operation):  # Type: 0
    print(operation)


def update_profile(operation):  # Type: 1
    print(operation)


def update_settings(operation):  # Type: 36
    print(operation)


def notified_update_profile(operation):  # Type: 2
    print(operation)


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
    print(operation)


def notified_update_group(operation):  # Type: 11
    print(operation)


def invite_into_group(operation):  # Type: 12
    print(operation)


def notified_invite_into_group(operation):  # Type: 13
    print(operation)


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
    print(operation)


def reject_group_invitation(operation):  # Type: 34
    print(operation)


def notified_reject_group_invitation(operation):  # Type: 35
    print(operation)


def kickout_from_group(operation):  # Type: 18
    print(operation)


def notified_kickout_from_group(operation):  # Type: 19
    print(operation)


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
    print(operation)


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
    print(operation)


def failed_email_confirmation(operation):  # Type: 56
    print(operation)


def notified_chat_content(operation):  # Type: 58
    print(operation)


def notified_push_noticenter_item(operation):  # Type: 59
    print(operation)


def notified_join_chat(operation):  # Type: 60
    print(operation)


def notified_leave_chat(operation):  # Type: 61
    print(operation)


def notified_typing(operation):  # Type: 62
    print(operation)


def friend_request_accepted(operation):  # Type: 63
    print(operation)


def destory_message(operation):  # Type: 64
    print(operation)


def notified_destory_message(operation):  # Type: 65
    print(operation)


def update_publickeychain(operation):  # Type: 66
    print(operation)


def notified_update_publickeychain(operation):  # Type: 67
    print(operation)


def notified_block_contact(operation):  # Type: 68
    print(operation)


def notified_unblock_contact(operation):  # Type: 69
    print(operation)


def update_grouppreference(operation):  # Type: 70
    print(operation)


def notified_payment_event(operation):  # Type: 71
    print(operation)


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


def update_timeline_settings(operation):  # Type: 87
    print(operation)


def notified_friend_request(operation):  # Type: 88
    print(operation)


def update_ringback_tone(operation):  # Type: 89
    print(operation)


def notified_postback(operation):  # Type: 90
    print(operation)


def receive_read_watermark(operation):  # Type: 91
    print(operation)


def notified_message_delivered(operation):  # Type: 92
    print(operation)


def notified_update_chat_bar(operation):  # Type: 93
    print(operation)


def notified_chatapp_installed(operation):  # Type: 94
    print(operation)


def notified_chatapp_updated(operation):  # Type: 95
    print(operation)


def notified_chat_app_new_mark(operation):  # Type: 96
    print(operation)


def notified_chatapp_deleted(operation):  # Type: 97
    print(operation)


def notified_chatapp_sync(operation):  # Type: 98
    print(operation)


def notified_update_message(operation):  # Type: 99
    print(operation)


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
    OpType.SEND_CHAT_CHECKED: send_chat_checked,
    OpType.SEND_CHAT_REMOVED: send_chat_removed,
    OpType.NOTIFIED_FORCE_SYNC: notified_force_sync,
    OpType.SEND_CONTENT: send_content,
    OpType.SEND_MESSAGE_MYHOME: send_message_myhome,
    OpType.NOTIFIED_UPDATE_CONTENT_PREVIEW: notified_update_content_preview,
    OpType.REMOVE_ALL_MESSAGES: remove_all_messages,
    OpType.NOTIFIED_UPDATE_PURCHASES: notified_update_purchases,
    OpType.DUMMY: dummy,
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
    OpType.DESTROY_MESSAGE: destory_message,
    OpType.NOTIFIED_DESTROY_MESSAGE: notified_destory_message,
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

if __name__ == '__main__':
    while True:
        oepoll.trace()
