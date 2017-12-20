function init() {
  var scene = new THREE.Scene();

  // camera
  var camera = new THREE.PerspectiveCamera(
    45,
    window.innerWidth / window.innerHeight,
    1,
    1000
  );
  camera.position.z = 30;
  camera.position.x = 0;
  camera.position.y = 20;
  camera.lookAt(new THREE.Vector3(0, 0, 0));

  var texture = new THREE.CanvasTexture(generateTexture());
  texture.needsUpdate = true;

  function generateTexture() {
    var size = 4;

    var canvas = document.createElement("canvas");
    canvas.width = size;
    canvas.height = size;

    var context = canvas.getContext("2d");
    var gradient = context.createRadialGradient(
      canvas.width / 2,
      canvas.height / 2,
      0,
      canvas.width / 2,
      canvas.height / 2,
      canvas.width / 2
    );
    gradient.addColorStop(0, "rgba(176,35,54,1)"); //0
    gradient.addColorStop(0.2, "rgba(176,35,54,1)"); //0.2
    gradient.addColorStop(0.4, "rgba(176,35,54,1)"); // 0.4
    gradient.addColorStop(1, "rgba(0,0,0,0)"); //1

    context.fillStyle = gradient;
    context.fillRect(0, 0, canvas.width, canvas.height);

    return canvas;
  }

  var material = new THREE.PointsMaterial({
    color: "rgb(255, 255, 255)",
    size: 0.25,
    map: texture,
    transparent: true,
    blending: THREE.AdditiveBlending,
    depthWrite: false
  });

  var geometry = new THREE.SphereGeometry(10, 84, 84);

  geometry.vertices.forEach(function(vertex) {
    vertex.x += Math.random() - 0.15;
    vertex.y += Math.random() - 0.15;
    vertex.z += Math.random() - 0.15;
  });

  var particles = new THREE.Points(geometry, material);
  particles.name = "particles";

  scene.add(particles);

  var renderer = new THREE.WebGLRenderer();
  renderer.setSize(window.innerWidth, window.innerHeight);

  var controls = new THREE.OrbitControls(camera, renderer.domElement);

  document.getElementById("webgl").appendChild(renderer.domElement);


  update(renderer, scene, camera, controls);

  return scene;
}


function update(renderer, scene, camera, controls) {
  controls.update();

  renderer.render(scene, camera);

  var particles = scene.getObjectByName("particles");
  particles.rotation.y += 0.005;

  requestAnimationFrame(function() {
    update(renderer, scene, camera, controls);
  });
}

var scene = init();
