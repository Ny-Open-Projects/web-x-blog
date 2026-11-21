class Plugin:
    plugins = []

    def __init_subclass__(cls, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.slug = name or cls.__name__.lower()
        Plugin.plugins.append(cls)

class EmailPlugin(Plugin, name="email"):
    def run(self):
        return "sending email"

class SmsPlugin(Plugin):
    def run(self):
        return "sending sms"

if __name__ == "__main__":
    for p in Plugin.plugins:
        print(p.slug, "->", p().run())
    print(EmailPlugin.slug)
