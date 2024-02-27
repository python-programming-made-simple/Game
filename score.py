import load

def increase_score(asteroid,score_image):
    load.asteroids.remove(asteroid)
    load.score = load.score + 1
    if load.score != 10:
        load.point_sound.play()
    score_image.display(str(load.score))