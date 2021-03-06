import appdaemon.plugins.hass.hassapi as hass

class mute_ads(hass.Hass):

    def initialize(self):
        for media_player in self.args["media_players"]:
            self.listen_state(self.handle_mute, media_player, attribute = "media_title")

    def handle_mute(self, entity, attribute, old, new, kwargs):
        self.log("old media_title: %s, new media_title: %s" % (old, new))
        if new != old:
            if new == "":
                self.call_service("media_player/volume_mute", entity_id=entity, is_volume_muted=True)
            if old == "":
                self.call_service("media_player/volume_mute", entity_id=entity, is_volume_muted=False)

