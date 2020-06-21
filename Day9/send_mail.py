def send_mail(text='EMail Body', subject="Hello World", to_emails=None):
	assert isinstance(to_emails, list)
