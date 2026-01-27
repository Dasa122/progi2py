class StreamerChannel:
    def __init__(self, name, platform, viewers, followers, category):
        self.name = name
        self.platform = platform
        self.viewers = viewers
        self.followers = followers
        self.category = category
        self.rank = 1
        self.growth_points = 0

    def __str__(self):
        return f"{self.name} csatorna: platform={self.platform}, viewers={self.viewers}, followers={self.followers}, category={self.category}, rank={self.rank}, growth={self.growth_points}"

    def is_popular(self):
        return self.viewers > 10000

    def is_trending(self):
        return self.followers > 50000

    def rank_up(self):
        self.rank += 1
        self.growth_points = 0

    def gain_growth(self, points):
        self.growth_points += points
        if self.growth_points >= 100:
            self.rank_up()

    def save_info(self, filename):
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(str(self) + '\n')


channels = []

def top_viewers():
    if not channels:
        return False
    max_viewers = max(c.viewers for c in channels)
    return max_viewers

def create_channels():
    ch1 = StreamerChannel("RagePlay", "Twitch", 25000, 120000, "FPS")
    ch2 = StreamerChannel("CozyCorner", "YouTube", 8000, 45000, "Just Chatting")
    ch3 = StreamerChannel("SpeedRunner", "Twitch", 15000, 60000, "Speedrun")
    ch4 = StreamerChannel("IndieGamer", "Mixer", 3000, 15000, "Indie")
    ch5 = StreamerChannel("ProStrategy", "Twitch", 40000, 200000, "Strategy")
    channels.extend([ch1, ch2, ch3, ch4, ch5])

def main():
    create_channels()
    print("Népszerű csatornák (viewers > 10000):")
    for c in channels:
        if c.is_popular():
            print(c)

    print("\nTrendelő csatornák (followers > 50000):")
    for c in channels:
        if c.is_trending():
            print(c)

    print("\nLegnézettebb csatornák:")
    top = top_viewers()
    for c in channels:
        if top and c.viewers == top:
            print(c)

    for c in channels:
        c.save_info("streamer_info.txt")


main()
