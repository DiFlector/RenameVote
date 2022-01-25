from django import forms


class RegistrationForm(forms.Form):
    template_name_label = ""
    name = forms.CharField(max_length=1000, min_length=0,
                            required=True, widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Полное Имя', 'class' : 'p-3 shadow block w-full dark:bg-zinc-800 mt-5'
                                    }
                                )
                            )
    login = forms.CharField(max_length=1000, min_length=0,
                            required=True, widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Логин', 'class' : 'p-3 shadow block w-full dark:bg-zinc-800 mt-5'
                                    }
                                )
                            )
    email = forms.CharField(max_length=1000, min_length=0,
                            required=True, widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'E-mail', 'class' : 'p-3 shadow block w-full dark:bg-zinc-800 mt-5'
                                    }
                                )
                            )
    phone = forms.CharField(max_length=1000, min_length=0,
                            required=True, widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Телефон', 'class' : 'p-3 shadow block w-full dark:bg-zinc-800 mt-5'
                                    }
                                )
                            )
    password = forms.CharField(max_length=1000, min_length=0,
                            required=True, widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Пароль', 'class' : 'p-3 shadow block w-full dark:bg-zinc-800 mt-5'
                                    }
                                )
                            )
    confirm_password = forms.CharField(max_length=1000, min_length=0,
                            required=True, widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Подтверждение пароля', 'class' : 'p-3 shadow block w-full dark:bg-zinc-800 mt-5'
                                    }
                                )
                            )


class AuthorizationForm(forms.Form):
    template_name_label = ""
    login = forms.CharField(max_length=1000, min_length=0,
                            required=True, widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Имя пользователя', 'class' : 'p-3 shadow block w-full dark:bg-zinc-800 mt-3'
                                    }
                                )
                            )
    password = forms.CharField(max_length=1000, min_length=0,
                            required=True, widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Пароль', 'class' : 'p-3 shadow block w-full dark:bg-zinc-800 mt-5'
                                    }
                                )
                            )


class VotingForm(forms.Form):
    type = forms.BooleanField()
    name = forms.CharField()


class AnswerForm(forms.Form):
    text = forms.CharField()
