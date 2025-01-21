def check_collision(player, obj):
    return (player.x < obj.x + obj.width and
            player.x + player.width > obj.x and
            player.y < obj.y + obj.height and
            player.y + player.height > obj.y)