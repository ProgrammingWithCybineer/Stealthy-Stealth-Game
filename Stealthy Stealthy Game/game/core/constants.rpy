init python:

    #################################################
    # Screen Settings
    #################################################

    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    TILE_SIZE = 32

    #################################################
    # Player Settings
    #################################################

    PLAYER_START_X = 100
    PLAYER_START_Y = 100

    PLAYER_WALK_SPEED = 3
    PLAYER_RUN_SPEED = 6
    PLAYER_CROUCH_SPEED = 2

    PLAYER_HEALTH = 100

    #################################################
    # Stealth Settings
    #################################################

    MAX_VISIBILITY = 100
    MIN_VISIBILITY = 0

    SHADOW_BONUS = 50
    HIDING_BONUS = 40

    DETECTION_THRESHOLD = 75

    #################################################
    # Noise Settings
    #################################################

    WALK_NOISE = 50
    RUN_NOISE = 150
    CROUCH_NOISE = 20

    THROWN_OBJECT_NOISE = 300

    #################################################
    # Guard Settings
    #################################################

    DEFAULT_GUARD_SPEED = 3
    #guard.speed = DEFAULT_GUARD_SPEED

    DEFAULT_VISION_RANGE = 200
    ELITE_VISION_RANGE = 300
    BOSS_VISION_RANGE = 500

    DEFAULT_HEARING_RANGE = 250
    ELITE_HEARING_RANGE = 400

    GUARD_CAPTURE_DISTANCE = 25

    #################################################
    # AI Timers
    #################################################

    SEARCH_TIME = 300

    INVESTIGATION_TIME = 180

    ALERT_TIME = 600

    #################################################
    # Camera Settings
    #################################################

    CAMERA_ROTATION_SPEED = 2

    CAMERA_VISION_RANGE = 250

    CAMERA_ALERT_TIME = 1

    #################################################
    # Drone Settings
    #################################################

    DRONE_SPEED = 2

    DRONE_VISION_RANGE = 275

    #################################################
    # Smoke Grenades
    #################################################

    SMOKE_RADIUS = 250

    SMOKE_DURATION = 15

    #################################################
    # EMP Settings
    #################################################

    EMP_RADIUS = 300

    EMP_DURATION = 20

    #################################################
    # Lockpicking
    #################################################

    LOCKPICK_MAX_DURABILITY = 10

    LOCK_DIFFICULTY_EASY = 1
    LOCK_DIFFICULTY_MEDIUM = 2
    LOCK_DIFFICULTY_HARD = 3

    #################################################
    # Hacking
    #################################################

    FIREWALL_EASY = 3
    FIREWALL_MEDIUM = 5
    FIREWALL_HARD = 8

    TRACE_LIMIT = 100

    #################################################
    # Mission Scoring
    #################################################

    DETECTION_PENALTY = 100

    ALARM_PENALTY = 250

    KNOCKOUT_PENALTY = 50

    GHOST_BONUS = 1000

    #################################################
    # Rankings
    #################################################

    RANK_GHOST = "Ghost"
    RANK_SILENT_ASSASSIN = "Silent Assassin"
    RANK_MASTER_THIEF = "Master Thief"
    RANK_ELITE_OPERATIVE = "Elite Operative"

    #################################################
    # Procedural Generation
    #################################################

    CASTLE_MIN_ROOMS = 10

    CASTLE_MAX_ROOMS = 30

    TREASURE_ROOM_CHANCE = 20

    SECRET_ROOM_CHANCE = 10

    #################################################
    # Boss Settings
    #################################################

    BOSS_HEALTH = 500

    BOSS_SPEED = 4

    BOSS_DAMAGE = 25

    #################################################
    # Checkpoints
    #################################################

    MAX_CHECKPOINTS = 10

    #################################################
    # Inventory
    #################################################

    MAX_INVENTORY_SIZE = 20

    #################################################
    # Gadget Cooldowns
    #################################################

    SMOKE_COOLDOWN = 30

    EMP_COOLDOWN = 60

    NIGHT_VISION_BATTERY = 300

    #################################################
    # UI
    #################################################

    HUD_X = 10
    HUD_Y = 10

    MINIMAP_X = 1000
    MINIMAP_Y = 20

    OBJECTIVE_X = 20
    OBJECTIVE_Y = 100

    #################################################
    # Save System
    #################################################

    AUTOSAVE_INTERVAL = 300   